import base64
import logging
from copy import copy
from pathlib import Path
from typing import Union

import yaml
from linkml_runtime import SchemaView
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.processing.referencevalidator import ReferenceValidator
from linkml_runtime.utils.introspection import package_schemaview
from pydantic import BaseModel

from gsvr.datamodel import VariableCollection, Variable, MAIN_SCHEMA_PATH, UnitOfMeasure, VariableRelationship

logger = logging.getLogger(__name__)

descriptive_name_to_ucum_mapping = {
    "Inch": "[in_i]"
}

class InferenceEngine(BaseModel):
    """
    Inference engine for generating inferred variables
    """

    def materialize(self, collection: VariableCollection) -> VariableCollection:
        """
        Generates an inferred collection
        """
        inferred = copy(collection)
        inferred.variables = {}
        for var in collection.variables.values():
            self.add_variable(var, inferred)
        return inferred

    def add_variable(self, var: Variable, collection: VariableCollection) -> Variable:
        if var.name in collection.variables:
            self.merge_variables(var, collection.variables[var.name])
            collection.variables[var.name] = var
        else:
            collection.variables[var.name] = var
        var.pid = base64.b64encode(bytes(var.name, 'utf-8'))
        for subvar in var.subtypes.values():
            subvar = self.add_variable(subvar, collection)
            subvar.relationships.append(VariableRelationship(predicate="todo",
                                                             object=var.name))
            logger.info(f"ADDINGG {subvar.name} REL {subvar.relationships}")
        var.subtypes = []
        for subvar in var.variable_forms.values():
            subvar = self.add_variable(subvar, collection)
            subvar.relationships.append(VariableRelationship(predicate="todo",
                                                             object=var.name))
        var.variable_forms = []
        for u in var.allowed_units:
            logger.info(f"Materializing unit {u} for {var.name}")
            if u in descriptive_name_to_ucum_mapping:
                ucum_code = descriptive_name_to_ucum_mapping[u]
                symbol = u
            else:
                ucum_code = u
                symbol = u
            new_var = Variable(name=f"{var.name}_unit_{symbol}",
                               unit=UnitOfMeasure(ucum_code=ucum_code,
                                                  symbol=symbol))
            self.add_variable(new_var, collection)
        return collection.variables[var.name]


    def merge_variables(self, target: Variable, source: Variable):
        """
        Merges source into target.
        """
        logger.info(f"Merging: {target.name}")
        for k, v in source.__dict__.items():
            if not v:
                continue
            curr = getattr(target, k, None)
            if curr and curr != v:
                logger.error(f"{target.name}.{k} {curr} != {v}")
            setattr(target, k, v)

    def load(self, path: Union[Path, str]) -> VariableCollection:
        """
        Load a VariableCollection from a YAML file.
        """
        logger.info(f"Loading {path}")
        with open(str(path)) as f:
            do = yaml.safe_load(f)
        sv = SchemaView(str(MAIN_SCHEMA_PATH))
        normalizer = ReferenceValidator(sv, expand_all=True)
        logger.info("Normalizing")
        norm_do = normalizer.normalize(do, target=VariableCollection.__name__)
        obj = VariableCollection(**norm_do)
        return obj

    def dump(self, vc: VariableCollection, path: Union[Path, str]):
        """
        Dump a VariableCollection to a YAML file.
        """
        with open(str(path), "w", encoding="utf-8") as f:
            yaml.dump(vc.dict(exclude_unset=True), f)

