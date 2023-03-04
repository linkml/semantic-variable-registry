# Auto generated from badm-soil.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-05T22:20:16
# Schema: gsvr-badm-soil
#
# id: https://w3id.org/gsvr/badm-soil
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BADM = CurieNamespace('badm', 'https://w3id.org/gsvr/badm-soil/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = BADM


# Types

# Class references




# Enumerations
class PROFILEZEROREF(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="See additional information in Approach / Comments")

    _defn = EnumDefinition(
        name="PROFILEZEROREF",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Top of mineral soil",
                PermissibleValue(text="Top of mineral soil",
                                 description="Top of mineral soil not including organic layers") )
        setattr(cls, "Top of surface",
                PermissibleValue(text="Top of surface",
                                 description="On top of all organic layers") )

class SOILCLASSTAXON(EnumDefinitionImpl):

    NRCS = PermissibleValue(text="NRCS")
    Other = PermissibleValue(text="Other",
                                 description="See additional information in Approach / Comments")
    WRB = PermissibleValue(text="WRB",
                             description="Previously FAO")

    _defn = EnumDefinition(
        name="SOILCLASSTAXON",
    )

class SOILGROUP(EnumDefinitionImpl):

    Acrisol = PermissibleValue(text="Acrisol")
    Albeluvisol = PermissibleValue(text="Albeluvisol")
    Alisol = PermissibleValue(text="Alisol")
    Andosol = PermissibleValue(text="Andosol")
    Anthrosol = PermissibleValue(text="Anthrosol")
    Arenosol = PermissibleValue(text="Arenosol")
    Calcisol = PermissibleValue(text="Calcisol")
    Cambisol = PermissibleValue(text="Cambisol")
    Chernozem = PermissibleValue(text="Chernozem")
    Cryosol = PermissibleValue(text="Cryosol")
    Durisol = PermissibleValue(text="Durisol")
    Ferralsol = PermissibleValue(text="Ferralsol")
    Fluvisol = PermissibleValue(text="Fluvisol")
    Gleysol = PermissibleValue(text="Gleysol")
    Gypsisol = PermissibleValue(text="Gypsisol")
    Histosol = PermissibleValue(text="Histosol")
    Kastanozem = PermissibleValue(text="Kastanozem")
    Leptosol = PermissibleValue(text="Leptosol")
    Lixisol = PermissibleValue(text="Lixisol")
    Luvisol = PermissibleValue(text="Luvisol")
    Nitisol = PermissibleValue(text="Nitisol")
    Phaeozem = PermissibleValue(text="Phaeozem")
    Planosol = PermissibleValue(text="Planosol")
    Plinthosol = PermissibleValue(text="Plinthosol")
    Podzol = PermissibleValue(text="Podzol")
    Regosol = PermissibleValue(text="Regosol")
    Solonchak = PermissibleValue(text="Solonchak")
    Solonetz = PermissibleValue(text="Solonetz")
    Technosol = PermissibleValue(text="Technosol")
    Umbrisol = PermissibleValue(text="Umbrisol")
    Vertisol = PermissibleValue(text="Vertisol")

    _defn = EnumDefinition(
        name="SOILGROUP",
    )

class SOILORDER(EnumDefinitionImpl):

    Alfisols = PermissibleValue(text="Alfisols")
    Andisols = PermissibleValue(text="Andisols")
    Aridisols = PermissibleValue(text="Aridisols")
    Entisols = PermissibleValue(text="Entisols")
    Gelisols = PermissibleValue(text="Gelisols")
    Histosols = PermissibleValue(text="Histosols")
    Inceptisols = PermissibleValue(text="Inceptisols")
    Mollisols = PermissibleValue(text="Mollisols")
    Oxisols = PermissibleValue(text="Oxisols")
    Spodosols = PermissibleValue(text="Spodosols")
    Ultisols = PermissibleValue(text="Ultisols")
    Vertisols = PermissibleValue(text="Vertisols")

    _defn = EnumDefinition(
        name="SOILORDER",
    )

class STATISTIC(EnumDefinitionImpl):

    Maximum = PermissibleValue(text="Maximum",
                                     description="Maximum value")
    Mean = PermissibleValue(text="Mean",
                               description="Average (mean) value of sample population")
    Minimum = PermissibleValue(text="Minimum",
                                     description="Minimum value")

    _defn = EnumDefinition(
        name="STATISTIC",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10th Percentile",
                PermissibleValue(text="10th Percentile",
                                 description="Quantile at 10% of distribution") )
        setattr(cls, "1st Percentile",
                PermissibleValue(text="1st Percentile",
                                 description="Quantile at 1% of distribution") )
        setattr(cls, "25th Percentile",
                PermissibleValue(text="25th Percentile",
                                 description="Quantile at 25% of distribution") )
        setattr(cls, "5th Percentile",
                PermissibleValue(text="5th Percentile",
                                 description="Quantile at 5% of distribution") )
        setattr(cls, "75th Percentile",
                PermissibleValue(text="75th Percentile",
                                 description="Quantile at 75% of distribution") )
        setattr(cls, "90th Percentile",
                PermissibleValue(text="90th Percentile",
                                 description="Quantile at 90% of distribution") )
        setattr(cls, "95th Percentile",
                PermissibleValue(text="95th Percentile",
                                 description="Quantile at 95% of distribution") )
        setattr(cls, "99th Percentile",
                PermissibleValue(text="99th Percentile",
                                 description="Quantile at 99% of distribution") )
        setattr(cls, "Measurement Uncertainty",
                PermissibleValue(text="Measurement Uncertainty",
                                 description="Report uncertainty as a plus or minus value in the measurement units. For example, enter 1.5 for +/- 1.5 units. Uncertainty may be reported from the instrument's specifications, determined empirically, or estimated by the tower team. Please describe such details in Approach. For uncertainty values that are better described by a range, a percent, or other, please enter information in Comments.") )
        setattr(cls, "Median - 50th Percentile",
                PermissibleValue(text="Median - 50th Percentile",
                                 description="Median - Quantile at 50% of distribution") )
        setattr(cls, "Single observation",
                PermissibleValue(text="Single observation",
                                 description="Single observation that is not a calculated statistic of replicates either to get a robust estimate or for spatial variability analysis. For example a single biomass observation may be the vegetation harvested in a single 1 x 1 meter area.") )
        setattr(cls, "Standard Deviation",
                PermissibleValue(text="Standard Deviation",
                                 description="Standard deviation may be reported from a sample population that consists of individual or aggregated samples (observations). If the distinction is important, specify in STATISTIC_METHOD or Comments.") )

class STATISTICMETHOD(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="STATISTICMETHOD",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Aggregate of individual observations",
                PermissibleValue(text="Aggregate of individual observations",
                                 description="The statistic is aggregated from individual observations located within the site. Observations may be grouped into sample areas (e.g., plots) within the site but those groupings are ignored. Statistics generated from individual observations directly yield information on the site generally. The statistic may represent spatial characteristics of the measurement within the site (e.g., spatial heterogeneity) and/or characteristics due to other factors (e.g., population variability).") )
        setattr(cls, "Aggregate of sample aggregates",
                PermissibleValue(text="Aggregate of sample aggregates",
                                 description="The statistic is aggregated from aggregated individual observations located in sample areas within the site. For example, individual observations are made in 5 sample plots within a site. "Aggregate of sample aggregates" is used if a plot statistic (e.g., Mean) is first calculated, and then the plot values are aggregated to calculate the site statistic. Statistics generated by this approach are often used to highlight the spatial characteristics within the site (i.e., the spatial heterogeneity of measurement within the site).") )
        setattr(cls, "Expert estimate",
                PermissibleValue(text="Expert estimate",
                                 description="Estimate made by expert familiar with site") )

class UNITSWC(EnumDefinitionImpl):

    Gravimetric = PermissibleValue(text="Gravimetric")
    Volumetric = PermissibleValue(text="Volumetric")

    _defn = EnumDefinition(
        name="UNITSWC",
    )

# Slots
class slots:
    pass

