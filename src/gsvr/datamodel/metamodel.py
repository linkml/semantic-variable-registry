from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal

metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'
    
class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True, 
                validate_all = True, 
                underscore_attrs_are_private = True, 
                extra = 'forbid', 
                arbitrary_types_allowed = True):
    pass                    


class VariableCategoryEnum(str, Enum):
    
    UNSPECIFIED = "UNSPECIFIED"
    GROUPING = "GROUPING"
    UNIT_UNSPECIFIED = "UNIT_UNSPECIFIED"
    UNIT = "UNIT"
    MEASUREMENT_VERBATIM = "MEASUREMENT_VERBATIM"
    MEASUREMENT_OBJECT = "MEASUREMENT_OBJECT"
    VERBATIM = "VERBATIM"
    ANCILLARY = "ANCILLARY"
    CATEGORICAL = "CATEGORICAL"
    CATEGORICAL_ORDINAL = "CATEGORICAL_ORDINAL"
    
    

class PvFormulaOptions(str, Enum):
    
    CODE = "CODE"
    CURIE = "CURIE"
    URI = "URI"
    FHIR_CODING = "FHIR_CODING"
    
    

class PresenceEnum(str, Enum):
    
    UNCOMMITTED = "UNCOMMITTED"
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    
    

class RelationalRoleEnum(str, Enum):
    
    SUBJECT = "SUBJECT"
    OBJECT = "OBJECT"
    PREDICATE = "PREDICATE"
    NODE = "NODE"
    OTHER_ROLE = "OTHER_ROLE"
    
    

class AliasPredicateEnum(str, Enum):
    
    EXACT_SYNONYM = "EXACT_SYNONYM"
    RELATED_SYNONYM = "RELATED_SYNONYM"
    BROAD_SYNONYM = "BROAD_SYNONYM"
    NARROW_SYNONYM = "NARROW_SYNONYM"
    
    

class CodeableConcept(ConfiguredBaseModel):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class Variable(CodeableConcept):
    
    pid: Optional[str] = Field(None, description="""a unique persistent identifier, used to unambiguously identify this concept""")
    structured_descriptions: Optional[str] = Field(None)
    description_as_question: Optional[str] = Field(None, description="""the description of the variable as presented as a question to the agent recording the measurement""")
    aliases: Optional[List[str]] = Field(default_factory=list)
    structured_aliases: Optional[str] = Field(None)
    category: Optional[VariableCategoryEnum] = Field(None)
    variable_forms: Optional[Dict[str, Variable]] = Field(default_factory=dict, description="""the same variable expressed different ways, for example, mass_in_kg is a variable form of mass""")
    subtypes: Optional[Dict[str, Variable]] = Field(default_factory=dict, description="""subtypes connecting a grouping variable to more specific ones""")
    numerator_variable: Optional[str] = Field(None, description="""for ratio variables, this is the variable that is the numerator.""")
    denominator_variable: Optional[str] = Field(None, description="""for ratio variables, this is the variable that is the denominator.""")
    unit: Optional[UnitOfMeasure] = Field(None)
    allowed_units: Optional[List[str]] = Field(default_factory=list)
    has_value_domain: Optional[str] = Field(None)
    relationships: Optional[List[VariableRelationship]] = Field(default_factory=list)
    status: Optional[str] = Field(None)
    quantity_type: Optional[str] = Field(None)
    embedded_value_set: Optional[AnonymousEnumExpression] = Field(None)
    named_value_set: Optional[str] = Field(None)
    allowed_named_value_sets: Optional[str] = Field(None)
    property_of: Optional[str] = Field(None)
    allowed_property_of: Optional[List[str]] = Field(default_factory=list)
    quantification_of: Optional[str] = Field(None)
    context: Optional[str] = Field(None)
    allowed_contexts: Optional[str] = Field(None)
    measured_in: Optional[str] = Field(None)
    allowed_measured_in: Optional[str] = Field(None)
    measured_using: Optional[List[str]] = Field(default_factory=list)
    aggregate_function: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class UnitLevelVariable(Variable):
    
    pid: Optional[str] = Field(None, description="""a unique persistent identifier, used to unambiguously identify this concept""")
    structured_descriptions: Optional[str] = Field(None)
    description_as_question: Optional[str] = Field(None, description="""the description of the variable as presented as a question to the agent recording the measurement""")
    aliases: Optional[List[str]] = Field(default_factory=list)
    structured_aliases: Optional[str] = Field(None)
    category: Optional[VariableCategoryEnum] = Field(None)
    variable_forms: Optional[Dict[str, Variable]] = Field(default_factory=dict, description="""the same variable expressed different ways, for example, mass_in_kg is a variable form of mass""")
    subtypes: Optional[Dict[str, Variable]] = Field(default_factory=dict, description="""subtypes connecting a grouping variable to more specific ones""")
    numerator_variable: Optional[str] = Field(None, description="""for ratio variables, this is the variable that is the numerator.""")
    denominator_variable: Optional[str] = Field(None, description="""for ratio variables, this is the variable that is the denominator.""")
    unit: Optional[UnitOfMeasure] = Field(None)
    allowed_units: Optional[List[str]] = Field(default_factory=list)
    has_value_domain: Optional[str] = Field(None)
    relationships: Optional[List[VariableRelationship]] = Field(default_factory=list)
    status: Optional[str] = Field(None)
    quantity_type: Optional[str] = Field(None)
    embedded_value_set: Optional[AnonymousEnumExpression] = Field(None)
    named_value_set: Optional[str] = Field(None)
    allowed_named_value_sets: Optional[str] = Field(None)
    property_of: Optional[str] = Field(None)
    allowed_property_of: Optional[List[str]] = Field(default_factory=list)
    quantification_of: Optional[str] = Field(None)
    context: Optional[str] = Field(None)
    allowed_contexts: Optional[str] = Field(None)
    measured_in: Optional[str] = Field(None)
    allowed_measured_in: Optional[str] = Field(None)
    measured_using: Optional[List[str]] = Field(default_factory=list)
    aggregate_function: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class VariableRelationship(ConfiguredBaseModel):
    
    predicate: Optional[str] = Field(None)
    object: str = Field(None)
    


class VariableCollection(ConfiguredBaseModel):
    
    code: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    structured_imports: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None)
    variables: Optional[Dict[str, Variable]] = Field(default_factory=dict)
    quantity_types: Optional[Dict[str, QuantityType]] = Field(default_factory=dict)
    measurables: Optional[Dict[str, Measurable]] = Field(default_factory=dict)
    physical_substances: Optional[Dict[str, PhysicalSubstance]] = Field(default_factory=dict)
    measurement_contexts: Optional[Dict[str, MeasurementContext]] = Field(default_factory=dict)
    devices: Optional[Dict[str, Device]] = Field(default_factory=dict)
    value_domains: Optional[Dict[str, ValueDomain]] = Field(default_factory=dict)
    


class QuantityType(CodeableConcept):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class PhysicalEntityOrPhenomena(CodeableConcept):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class PhysicalEntity(PhysicalEntityOrPhenomena):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class PhysicalSubstance(PhysicalEntity):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class Measurable(PhysicalEntity):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class MeasurementContext(PhysicalEntityOrPhenomena):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class Device(PhysicalEntity):
    
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class ValueDomain(CodeableConcept):
    
    uri: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    unique_name: Optional[str] = Field(None, description="""Formed by concatenating the collection code with the name.""")
    structured_mappings: Optional[List[StructuredMapping]] = Field(default_factory=list, description="""mappings from this variable concept to variables in other databases and concepts in other ontologies and vocabularies.""")
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sources: Optional[List[str]] = Field(default_factory=list)
    


class StructuredMapping(ConfiguredBaseModel):
    
    object_id: Optional[str] = Field(None)
    object_label: Optional[str] = Field(None)
    predicate_id: Optional[str] = Field(None)
    


class CommonMetadata(ConfiguredBaseModel):
    """
    Generic metadata shared across definitions
    """
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class MatchQuery(ConfiguredBaseModel):
    """
    A query that is used on an enum expression to dynamically obtain a set of permissivle values via a query that matches on properties of the external concepts
    """
    identifier_pattern: Optional[str] = Field(None, description="""A regular expression that is used to obtain a set of identifiers from a source_ontology to construct a set of permissible values""")
    source_ontology: Optional[str] = Field(None, description="""An ontology or vocabulary or terminology that is used in a query to obtain a set of permissible values""")
    


class ReachabilityQuery(ConfiguredBaseModel):
    """
    A query that is used on an enum expression to dynamically obtain a set of permissible values via walking from a set of source nodes to a set of descendants or ancestors over a set of relationship types
    """
    source_ontology: Optional[str] = Field(None, description="""An ontology or vocabulary or terminology that is used in a query to obtain a set of permissible values""")
    source_nodes: Optional[List[str]] = Field(default_factory=list, description="""A list of nodes that are used in the reachability query""")
    relationship_types: Optional[List[str]] = Field(default_factory=list, description="""A list of relationship types (properties) that are used in a reachability query""")
    is_direct: Optional[bool] = Field(None, description="""True if the reachability query should only include directly related nodes, if False then include also transitively connected""")
    include_self: Optional[bool] = Field(None, description="""True if the query is reflexive""")
    traverse_up: Optional[bool] = Field(None, description="""True if the direction of the reachability query is reversed and ancestors are retrieved""")
    


class Expression(ConfiguredBaseModel):
    """
    general mixin for any class that can represent some form of expression
    """
    None
    


class TypeExpression(Expression):
    
    pattern: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string""")
    structured_pattern: Optional[PatternExpression] = Field(None, description="""the string value of the slot must conform to the regular expression in the pattern expression""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    implicit_prefix: Optional[str] = Field(None, description="""Causes the slot value to be interpreted as a uriorcurie after prefixing with this string""")
    equals_string: Optional[str] = Field(None, description="""the slot must have range string and the value of the slot must equal the specified value""")
    equals_string_in: Optional[List[str]] = Field(default_factory=list, description="""the slot must have range string and the value of the slot must equal one of the specified values""")
    equals_number: Optional[int] = Field(None, description="""the slot must have range of a number and the value of the slot must equal the specified value""")
    minimum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or higher than this""")
    maximum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or lowe than this""")
    none_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    any_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    


class AnonymousTypeExpression(TypeExpression):
    
    pattern: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string""")
    structured_pattern: Optional[PatternExpression] = Field(None, description="""the string value of the slot must conform to the regular expression in the pattern expression""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    implicit_prefix: Optional[str] = Field(None, description="""Causes the slot value to be interpreted as a uriorcurie after prefixing with this string""")
    equals_string: Optional[str] = Field(None, description="""the slot must have range string and the value of the slot must equal the specified value""")
    equals_string_in: Optional[List[str]] = Field(default_factory=list, description="""the slot must have range string and the value of the slot must equal one of the specified values""")
    equals_number: Optional[int] = Field(None, description="""the slot must have range of a number and the value of the slot must equal the specified value""")
    minimum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or higher than this""")
    maximum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or lowe than this""")
    none_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    any_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    


class EnumExpression(Expression):
    """
    An expression that constrains the range of a slot
    """
    code_set: Optional[str] = Field(None, description="""the identifier of an enumeration code set.""")
    code_set_tag: Optional[str] = Field(None, description="""the version tag of the enumeration code set""")
    code_set_version: Optional[str] = Field(None, description="""the version identifier of the enumeration code set""")
    pv_formula: Optional[PvFormulaOptions] = Field(None, description="""Defines the specific formula to be used to generate the permissible values.""")
    permissible_values: Optional[Dict[str, PermissibleValue]] = Field(default_factory=dict, description="""A list of possible values for a slot range""")
    include: Optional[List[AnonymousEnumExpression]] = Field(default_factory=list, description="""An enum expression that yields a list of permissible values that are to be included, after subtracting the minus set""")
    minus: Optional[List[AnonymousEnumExpression]] = Field(default_factory=list, description="""An enum expression that yields a list of permissible values that are to be subtracted from the enum""")
    inherits: Optional[List[str]] = Field(default_factory=list, description="""An enum definition that is used as the basis to create a new enum""")
    reachable_from: Optional[ReachabilityQuery] = Field(None, description="""Specifies a query for obtaining a list of permissible values based on graph reachability""")
    matches: Optional[MatchQuery] = Field(None, description="""Specifies a match query that is used to calculate the list of permissible values""")
    concepts: Optional[List[str]] = Field(default_factory=list, description="""A list of identifiers that are used to construct a set of permissible values""")
    


class AnonymousEnumExpression(EnumExpression):
    """
    An enum_expression that is not named
    """
    code_set: Optional[str] = Field(None, description="""the identifier of an enumeration code set.""")
    code_set_tag: Optional[str] = Field(None, description="""the version tag of the enumeration code set""")
    code_set_version: Optional[str] = Field(None, description="""the version identifier of the enumeration code set""")
    pv_formula: Optional[PvFormulaOptions] = Field(None, description="""Defines the specific formula to be used to generate the permissible values.""")
    permissible_values: Optional[Dict[str, PermissibleValue]] = Field(default_factory=dict, description="""A list of possible values for a slot range""")
    include: Optional[List[AnonymousEnumExpression]] = Field(default_factory=list, description="""An enum expression that yields a list of permissible values that are to be included, after subtracting the minus set""")
    minus: Optional[List[AnonymousEnumExpression]] = Field(default_factory=list, description="""An enum expression that yields a list of permissible values that are to be subtracted from the enum""")
    inherits: Optional[List[str]] = Field(default_factory=list, description="""An enum definition that is used as the basis to create a new enum""")
    reachable_from: Optional[ReachabilityQuery] = Field(None, description="""Specifies a query for obtaining a list of permissible values based on graph reachability""")
    matches: Optional[MatchQuery] = Field(None, description="""Specifies a match query that is used to calculate the list of permissible values""")
    concepts: Optional[List[str]] = Field(default_factory=list, description="""A list of identifiers that are used to construct a set of permissible values""")
    


class SlotExpression(Expression):
    """
    an expression that constrains the range of values a slot can take
    """
    range: Optional[str] = Field(None, description="""defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2
""")
    range_expression: Optional[AnonymousClassExpression] = Field(None, description="""A range that is described as a boolean expression combining existing ranges""")
    enum_range: Optional[EnumExpression] = Field(None, description="""An inlined enumeration""")
    required: Optional[bool] = Field(None, description="""true means that the slot must be present in the loaded definition""")
    recommended: Optional[bool] = Field(None, description="""true means that the slot should be present in the loaded definition, but this is not required""")
    inlined: Optional[bool] = Field(None, description="""True means that keyed or identified slot appears in an outer structure by value.  False means that only the key or identifier for the slot appears within the domain, referencing a structure that appears elsewhere.""")
    inlined_as_list: Optional[bool] = Field(None, description="""True means that an inlined slot is represented as a list of range instances.  False means that an inlined slot is represented as a dictionary, whose key is the slot key or identifier and whose value is the range instance.""")
    minimum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or higher than this""")
    maximum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or lowe than this""")
    pattern: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string""")
    structured_pattern: Optional[PatternExpression] = Field(None, description="""the string value of the slot must conform to the regular expression in the pattern expression""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    implicit_prefix: Optional[str] = Field(None, description="""Causes the slot value to be interpreted as a uriorcurie after prefixing with this string""")
    value_presence: Optional[PresenceEnum] = Field(None, description="""if true then a value must be present (for lists there must be at least one value). If false then a value must be absent (for lists, must be empty)""")
    equals_string: Optional[str] = Field(None, description="""the slot must have range string and the value of the slot must equal the specified value""")
    equals_string_in: Optional[List[str]] = Field(default_factory=list, description="""the slot must have range string and the value of the slot must equal one of the specified values""")
    equals_number: Optional[int] = Field(None, description="""the slot must have range of a number and the value of the slot must equal the specified value""")
    equals_expression: Optional[str] = Field(None, description="""the value of the slot must equal the value of the evaluated expression""")
    minimum_cardinality: Optional[int] = Field(None, description="""the minimum number of entries for a multivalued slot""")
    maximum_cardinality: Optional[int] = Field(None, description="""the maximum number of entries for a multivalued slot""")
    has_member: Optional[AnonymousSlotExpression] = Field(None, description="""the value of the slot is multivalued with at least one member satisfying the condition""")
    all_members: Optional[AnonymousSlotExpression] = Field(None, description="""the value of the slot is multivalued with all members satisfying the condition""")
    none_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    any_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    


class ClassExpression(ConfiguredBaseModel):
    """
    A boolean expression that can be used to dynamically determine membership of a class
    """
    any_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    none_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    all_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    slot_conditions: Optional[Dict[str, SlotDefinition]] = Field(default_factory=dict, description="""expresses constraints on a group of slots for a class expression""")
    


class ClassLevelRule(ConfiguredBaseModel):
    """
    A rule that is applied to classes
    """
    None
    


class Setting(ConfiguredBaseModel):
    """
    assignment of a key to a value
    """
    setting_key: Optional[str] = Field(None, description="""the variable name for a setting""")
    setting_value: str = Field(None, description="""The value assigned for a setting""")
    


class Prefix(ConfiguredBaseModel):
    """
    prefix URI tuple
    """
    prefix_prefix: Optional[str] = Field(None, description="""the nsname (sans ':' for a given prefix)""")
    prefix_reference: str = Field(None, description="""A URI associated with a given prefix""")
    


class LocalName(ConfiguredBaseModel):
    """
    an attributed label
    """
    local_name_source: Optional[str] = Field(None, description="""the ncname of the source of the name""")
    local_name_value: str = Field(None, description="""a name assigned to an element in a given ontology""")
    


class Example(ConfiguredBaseModel):
    """
    usage example and description
    """
    value: Optional[str] = Field(None, description="""example value""")
    value_description: Optional[str] = Field(None, description="""description of what the value is doing""")
    value_object: Optional[Any] = Field(None, description="""direct object representation of the example""")
    


class AltDescription(ConfiguredBaseModel):
    """
    an attributed description
    """
    alt_description_source: Optional[str] = Field(None, description="""the source of an attributed description""")
    alt_description_text: str = Field(None, description="""text of an attributed description""")
    


class UnitOfMeasure(ConfiguredBaseModel):
    """
    A unit of measure, or unit, is a particular quantity value that has been chosen as a scale for measuring other quantities the same kind (more generally of equivalent dimension).
    """
    symbol: Optional[str] = Field(None, description="""name of the unit encoded as a symbol""")
    abbreviation: Optional[str] = Field(None, description="""An abbreviation for a unit is a short ASCII string that is used in place of the full name for the unit in contexts where non-ASCII characters would be problematic, or where using the abbreviation will enhance readability. When a power of a base unit needs to be expressed, such as squares this can be done using abbreviations rather than symbols (source: qudt)""")
    descriptive_name: Optional[str] = Field(None, description="""the spelled out name of the unit, for example, meter""")
    exact_mappings: Optional[List[str]] = Field(None, description="""Used to link a unit to equivalent concepts in ontologies such as UO, SNOMED, OEM, OBOE, NCIT""")
    ucum_code: Optional[str] = Field(None, description="""associates a QUDT unit with its UCUM code (case-sensitive).""")
    derivation: Optional[str] = Field(None, description="""Expression for deriving this unit from other units""")
    has_quantity_kind: Optional[str] = Field(None, description="""Concept in a vocabulary or ontology that denotes the kind of quanity being measured, e.g. length""")
    iec61360code: Optional[str] = Field(None)
    


class Annotatable(ConfiguredBaseModel):
    """
    mixin for classes that support annotations
    """
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    


class Extension(ConfiguredBaseModel):
    """
    a tag/value pair used to add non-model information to an entry
    """
    extension_tag: str = Field(None, description="""a tag associated with an extension""")
    extension_value: str = Field(None, description="""the actual annotation""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    


class Annotation(Extension, Annotatable):
    """
    a tag/value pair with the semantics of OWL Annotation
    """
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    extension_tag: str = Field(None, description="""a tag associated with an extension""")
    extension_value: str = Field(None, description="""the actual annotation""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    


class Extensible(ConfiguredBaseModel):
    """
    mixin for classes that support extension
    """
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    


class Element(Extensible, Annotatable, CommonMetadata):
    """
    a named element in the model
    """
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class SchemaDefinition(Element):
    """
    a collection of subset, type, slot, enum and class definitions
    """
    id: str = Field(None, description="""The official schema URI""")
    version: Optional[str] = Field(None, description="""particular version of schema""")
    imports: Optional[List[str]] = Field(default_factory=list, description="""other schemas that are included in this schema""")
    license: Optional[str] = Field(None, description="""license for the schema""")
    prefixes: Optional[List[Prefix]] = Field(default_factory=list, description="""prefix / URI definitions to be added to the context beyond those fetched from prefixcommons in id prefixes""")
    emit_prefixes: Optional[List[str]] = Field(default_factory=list, description="""a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.""")
    default_curi_maps: Optional[List[str]] = Field(default_factory=list, description="""ordered list of prefixcommon biocontexts to be fetched to resolve id prefixes and inline prefix variables""")
    default_prefix: Optional[str] = Field(None, description="""default and base prefix -- used for ':' identifiers, @base and @vocab""")
    default_range: Optional[str] = Field(None, description="""default slot range to be used if range element is omitted from a slot definition""")
    subsets: Optional[Dict[str, SubsetDefinition]] = Field(default_factory=dict, description="""An index to the collection of all subset definitions in the schema""")
    types: Optional[Dict[str, TypeDefinition]] = Field(default_factory=dict, description="""An index to the collection of all type definitions in the schema""")
    enums: Optional[Dict[str, EnumDefinition]] = Field(default_factory=dict, description="""An index to the collection of all enum definitions in the schema""")
    slot_definitions: Optional[Dict[str, SlotDefinition]] = Field(default_factory=dict, description="""An index to the collection of all slot definitions in the schema""")
    classes: Optional[Dict[str, ClassDefinition]] = Field(default_factory=dict, description="""An index to the collection of all class definitions in the schema""")
    metamodel_version: Optional[str] = Field(None, description="""Version of the metamodel used to load the schema""")
    source_file: Optional[str] = Field(None, description="""name, uri or description of the source of the schema""")
    source_file_date: Optional[datetime ] = Field(None, description="""modification date of the source of the schema""")
    source_file_size: Optional[int] = Field(None, description="""size in bytes of the source of the schema""")
    generation_date: Optional[datetime ] = Field(None, description="""date and time that the schema was loaded/generated""")
    slot_names_unique: Optional[bool] = Field(None, description="""if true then induced/mangled slot names are not created for class_usage and attributes""")
    settings: Optional[List[Setting]] = Field(default_factory=list, description="""A collection of global variable settings""")
    categories: Optional[List[str]] = Field(default_factory=list, description="""controlled terms used to categorize an element""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords or tags used to describe the element""")
    name: Optional[str] = Field(None, description="""a unique name for the schema that is both human-readable and consists of only characters from the NCName set""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class TypeDefinition(Element, TypeExpression):
    """
    an element that whose instances are atomic scalar values that can be mapped to primitive types
    """
    typeof: Optional[str] = Field(None, description="""Names a parent type""")
    base: Optional[str] = Field(None, description="""python base type that implements this type definition""")
    type_uri: Optional[str] = Field(None, description="""The uri that defines the possible values for the type definition""")
    repr: Optional[str] = Field(None, description="""the name of the python object that implements this type definition""")
    union_of: Optional[List[str]] = Field(default_factory=list, description="""indicates that the domain element consists exactly of the members of the element in the range.""")
    pattern: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string""")
    structured_pattern: Optional[PatternExpression] = Field(None, description="""the string value of the slot must conform to the regular expression in the pattern expression""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    implicit_prefix: Optional[str] = Field(None, description="""Causes the slot value to be interpreted as a uriorcurie after prefixing with this string""")
    equals_string: Optional[str] = Field(None, description="""the slot must have range string and the value of the slot must equal the specified value""")
    equals_string_in: Optional[List[str]] = Field(default_factory=list, description="""the slot must have range string and the value of the slot must equal one of the specified values""")
    equals_number: Optional[int] = Field(None, description="""the slot must have range of a number and the value of the slot must equal the specified value""")
    minimum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or higher than this""")
    maximum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or lowe than this""")
    none_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    any_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[AnonymousTypeExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class SubsetDefinition(Element):
    """
    an element that can be used to group other metamodel elements
    """
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class Definition(Element):
    """
    abstract base class for core metaclasses
    """
    is_a: Optional[str] = Field(None, description="""A primary parent class or slot from which inheritable metaslots are propagated from. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded""")
    abstract: Optional[bool] = Field(None, description="""Indicates the class or slot cannot be directly instantiated and is intended for grouping and specifying core inherited metaslots""")
    mixin: Optional[bool] = Field(None, description="""Indicates the class or slot is intended to be inherited from without being an is_a parent. mixins should not be inherited from using is_a, except by other mixins.""")
    mixins: Optional[List[str]] = Field(default_factory=list, description="""A collection of secondary parent classes or slots from which inheritable metaslots are propagated from.""")
    apply_to: Optional[List[str]] = Field(default_factory=list, description="""Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.""")
    values_from: Optional[List[str]] = Field(default_factory=list, description="""The identifier of a \"value set\" -- a set of identifiers that form the possible values for the range of a slot. Note: this is different than 'subproperty_of' in that 'subproperty_of' is intended to be a single ontology term while 'values_from' is the identifier of an entire value set.  Additionally, this is different than an enumeration in that in an enumeration, the values of the enumeration are listed directly in the model itself. Setting this property on a slot does not guarantee an expansion of the ontological hiearchy into an enumerated list of possible values in every serialization of the model.""")
    created_by: Optional[str] = Field(None, description="""agent that created the element""")
    created_on: Optional[datetime ] = Field(None, description="""time at which the element was created""")
    last_updated_on: Optional[datetime ] = Field(None, description="""time at which the element was last updated""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    status: Optional[str] = Field(None, description="""status of the element""")
    string_serialization: Optional[str] = Field(None, description="""Used on a slot that stores the string serialization of the containing object. The syntax follows python formatted strings, with slot names enclosed in {}s. These are expanded using the values of those slots.
We call the slot with the serialization the s-slot, the slots used in the {}s are v-slots. If both s-slots and v-slots are populated on an object then the value of the s-slot should correspond to the expansion.
Implementations of frameworks may choose to use this property to either (a) PARSE: implement automated normalizations by parsing denormalized strings into complex objects (b) GENERARE: implement automated to_string labeling of complex objects
For example, a Measurement class may have 3 fields: unit, value, and string_value. The string_value slot may have a string_serialization of {value}{unit} such that if unit=cm and value=2, the value of string_value shouldd be 2cm""")
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class EnumDefinition(Definition, EnumExpression):
    """
    an element whose instances must be drawn from a specified set of permissible values
    """
    enum_uri: Optional[str] = Field(None, description="""URI of the enum that provides a semantic interpretation of the element in a linked data context. The URI may come from any namespace and may be shared between schemas""")
    code_set: Optional[str] = Field(None, description="""the identifier of an enumeration code set.""")
    code_set_tag: Optional[str] = Field(None, description="""the version tag of the enumeration code set""")
    code_set_version: Optional[str] = Field(None, description="""the version identifier of the enumeration code set""")
    pv_formula: Optional[PvFormulaOptions] = Field(None, description="""Defines the specific formula to be used to generate the permissible values.""")
    permissible_values: Optional[Dict[str, PermissibleValue]] = Field(default_factory=dict, description="""A list of possible values for a slot range""")
    include: Optional[List[AnonymousEnumExpression]] = Field(default_factory=list, description="""An enum expression that yields a list of permissible values that are to be included, after subtracting the minus set""")
    minus: Optional[List[AnonymousEnumExpression]] = Field(default_factory=list, description="""An enum expression that yields a list of permissible values that are to be subtracted from the enum""")
    inherits: Optional[List[str]] = Field(default_factory=list, description="""An enum definition that is used as the basis to create a new enum""")
    reachable_from: Optional[ReachabilityQuery] = Field(None, description="""Specifies a query for obtaining a list of permissible values based on graph reachability""")
    matches: Optional[MatchQuery] = Field(None, description="""Specifies a match query that is used to calculate the list of permissible values""")
    concepts: Optional[List[str]] = Field(default_factory=list, description="""A list of identifiers that are used to construct a set of permissible values""")
    is_a: Optional[str] = Field(None, description="""A primary parent class or slot from which inheritable metaslots are propagated from. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded""")
    abstract: Optional[bool] = Field(None, description="""Indicates the class or slot cannot be directly instantiated and is intended for grouping and specifying core inherited metaslots""")
    mixin: Optional[bool] = Field(None, description="""Indicates the class or slot is intended to be inherited from without being an is_a parent. mixins should not be inherited from using is_a, except by other mixins.""")
    mixins: Optional[List[str]] = Field(default_factory=list, description="""A collection of secondary parent classes or slots from which inheritable metaslots are propagated from.""")
    apply_to: Optional[List[str]] = Field(default_factory=list, description="""Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.""")
    values_from: Optional[List[str]] = Field(default_factory=list, description="""The identifier of a \"value set\" -- a set of identifiers that form the possible values for the range of a slot. Note: this is different than 'subproperty_of' in that 'subproperty_of' is intended to be a single ontology term while 'values_from' is the identifier of an entire value set.  Additionally, this is different than an enumeration in that in an enumeration, the values of the enumeration are listed directly in the model itself. Setting this property on a slot does not guarantee an expansion of the ontological hiearchy into an enumerated list of possible values in every serialization of the model.""")
    created_by: Optional[str] = Field(None, description="""agent that created the element""")
    created_on: Optional[datetime ] = Field(None, description="""time at which the element was created""")
    last_updated_on: Optional[datetime ] = Field(None, description="""time at which the element was last updated""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    status: Optional[str] = Field(None, description="""status of the element""")
    string_serialization: Optional[str] = Field(None, description="""Used on a slot that stores the string serialization of the containing object. The syntax follows python formatted strings, with slot names enclosed in {}s. These are expanded using the values of those slots.
We call the slot with the serialization the s-slot, the slots used in the {}s are v-slots. If both s-slots and v-slots are populated on an object then the value of the s-slot should correspond to the expansion.
Implementations of frameworks may choose to use this property to either (a) PARSE: implement automated normalizations by parsing denormalized strings into complex objects (b) GENERARE: implement automated to_string labeling of complex objects
For example, a Measurement class may have 3 fields: unit, value, and string_value. The string_value slot may have a string_serialization of {value}{unit} such that if unit=cm and value=2, the value of string_value shouldd be 2cm""")
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class StructuredAlias(Extensible, Annotatable, Expression, CommonMetadata):
    """
    object that contains meta data about a synonym or alias including where it came from (source) and its scope (narrow, broad, etc.)
    """
    literal_form: str = Field(None, description="""The literal lexical form of a structured alias""")
    alias_predicate: Optional[AliasPredicateEnum] = Field(None, description="""The relationship between an element and its alias """)
    categories: Optional[List[str]] = Field(default_factory=list, description="""The category or categories of an alias. This can be drawn from any relevant vocabulary""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class AnonymousExpression(Extensible, Annotatable, Expression, CommonMetadata):
    
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class PathExpression(Extensible, Annotatable, Expression, CommonMetadata):
    """
    An expression that describes an abstract path from an object to another through a sequence of slot lookups
    """
    followed_by: Optional[PathExpression] = Field(None, description="""in a sequential list, this indicates the next member""")
    none_of: Optional[List[PathExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    any_of: Optional[List[PathExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[PathExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    exactly_one_of: Optional[List[PathExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    reversed: Optional[bool] = Field(None, description="""true if the slot is to be inversed""")
    traverse: Optional[str] = Field(None, description="""the slot to traverse""")
    range_expression: Optional[AnonymousClassExpression] = Field(None, description="""A range that is described as a boolean expression combining existing ranges""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class AnonymousSlotExpression(AnonymousExpression, SlotExpression):
    
    range: Optional[str] = Field(None, description="""defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2
""")
    range_expression: Optional[AnonymousClassExpression] = Field(None, description="""A range that is described as a boolean expression combining existing ranges""")
    enum_range: Optional[EnumExpression] = Field(None, description="""An inlined enumeration""")
    required: Optional[bool] = Field(None, description="""true means that the slot must be present in the loaded definition""")
    recommended: Optional[bool] = Field(None, description="""true means that the slot should be present in the loaded definition, but this is not required""")
    inlined: Optional[bool] = Field(None, description="""True means that keyed or identified slot appears in an outer structure by value.  False means that only the key or identifier for the slot appears within the domain, referencing a structure that appears elsewhere.""")
    inlined_as_list: Optional[bool] = Field(None, description="""True means that an inlined slot is represented as a list of range instances.  False means that an inlined slot is represented as a dictionary, whose key is the slot key or identifier and whose value is the range instance.""")
    minimum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or higher than this""")
    maximum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or lowe than this""")
    pattern: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string""")
    structured_pattern: Optional[PatternExpression] = Field(None, description="""the string value of the slot must conform to the regular expression in the pattern expression""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    implicit_prefix: Optional[str] = Field(None, description="""Causes the slot value to be interpreted as a uriorcurie after prefixing with this string""")
    value_presence: Optional[PresenceEnum] = Field(None, description="""if true then a value must be present (for lists there must be at least one value). If false then a value must be absent (for lists, must be empty)""")
    equals_string: Optional[str] = Field(None, description="""the slot must have range string and the value of the slot must equal the specified value""")
    equals_string_in: Optional[List[str]] = Field(default_factory=list, description="""the slot must have range string and the value of the slot must equal one of the specified values""")
    equals_number: Optional[int] = Field(None, description="""the slot must have range of a number and the value of the slot must equal the specified value""")
    equals_expression: Optional[str] = Field(None, description="""the value of the slot must equal the value of the evaluated expression""")
    minimum_cardinality: Optional[int] = Field(None, description="""the minimum number of entries for a multivalued slot""")
    maximum_cardinality: Optional[int] = Field(None, description="""the maximum number of entries for a multivalued slot""")
    has_member: Optional[AnonymousSlotExpression] = Field(None, description="""the value of the slot is multivalued with at least one member satisfying the condition""")
    all_members: Optional[AnonymousSlotExpression] = Field(None, description="""the value of the slot is multivalued with all members satisfying the condition""")
    none_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    any_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class SlotDefinition(Definition, SlotExpression):
    """
    an element that describes how instances are related to other instances
    """
    singular_name: Optional[str] = Field(None, description="""a name that is used in the singular form""")
    domain: Optional[str] = Field(None, description="""defines the type of the subject of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts that X is an instance of C1
""")
    slot_uri: Optional[str] = Field(None, description="""predicate of this slot for semantic web application""")
    multivalued: Optional[bool] = Field(None, description="""true means that slot can have more than one value""")
    inherited: Optional[bool] = Field(None, description="""true means that the *value* of a slot is inherited by subclasses""")
    readonly: Optional[str] = Field(None, description="""If present, slot is read only.  Text explains why""")
    ifabsent: Optional[str] = Field(None, description="""function that provides a default value for the slot.  Possible values for this slot are defined in
linkml.utils.ifabsent_functions.default_library:
  * [Tt]rue -- boolean True
  * [Ff]alse -- boolean False
  * bnode -- blank node identifier
  * class_curie -- CURIE for the containing class
  * class_uri -- URI for the containing class
  * default_ns -- schema default namespace
  * default_range -- schema default range
  * int(value) -- integer value
  * slot_uri -- URI for the slot
  * slot_curie -- CURIE for the slot
  * string(value) -- string value""")
    list_elements_unique: Optional[bool] = Field(None, description="""If True, then there must be no duplicates in the elements of a multivalued slot""")
    list_elements_ordered: Optional[bool] = Field(None, description="""If True, then the order of elements of a multivalued slot is guaranteed to be preserved. If False, the order may still be preserved but this is not guaranteed""")
    shared: Optional[bool] = Field(None, description="""If True, then the relationship between the slot domain and range is many to one or many to many""")
    key: Optional[bool] = Field(None, description="""True means that the key slot(s) uniquely identify the elements within a single container""")
    identifier: Optional[bool] = Field(None, description="""True means that the key slot(s) uniquely identifies the elements. There can be at most one identifier or key per container""")
    designates_type: Optional[bool] = Field(None, description="""True means that the key slot(s) is used to determine the instantiation (types) relation between objects and a ClassDefinition""")
    alias: Optional[str] = Field(None, description="""the name used for a slot in the context of its owning class.  If present, this is used instead of the actual slot name.""")
    owner: Optional[str] = Field(None, description="""the \"owner\" of the slot. It is the class if it appears in the slots list, otherwise the declaring slot""")
    domain_of: Optional[List[str]] = Field(default_factory=list, description="""the class(es) that reference the slot in a \"slots\" or \"slot_usage\" context""")
    subproperty_of: Optional[str] = Field(None, description="""Ontology property which this slot is a subproperty of.  Note: setting this property on a slot does not guarantee an expansion of the ontological hiearchy into an enumerated list of possible values in every serialization of the model.""")
    symmetric: Optional[bool] = Field(None, description="""If s is symmetric, and i.s=v, then v.s=i""")
    reflexive: Optional[bool] = Field(None, description="""If s is reflexive, then i.s=i for all instances i""")
    locally_reflexive: Optional[bool] = Field(None, description="""If s is locally_reflexive, then i.s=i for all instances i where s is a class slot for the type of i""")
    irreflexive: Optional[bool] = Field(None, description="""If s is irreflexive, then there exists no i such i.s=i""")
    asymmetric: Optional[bool] = Field(None, description="""If s is antisymmetric, and i.s=v where i is different from v, v.s cannot have value i""")
    transitive: Optional[bool] = Field(None, description="""If s is transitive, and i.s=z, and s.s=j, then i.s=j""")
    inverse: Optional[str] = Field(None, description="""indicates that any instance of d s r implies that there is also an instance of r s' d""")
    is_class_field: Optional[bool] = Field(None, description="""indicates that for any instance, i, the domain of this slot will include an assertion of i s range""")
    transitive_form_of: Optional[str] = Field(None, description="""If s transitive_form_of d, then (1) s holds whenever d holds (2) s is transitive (3) d holds whenever s holds and there are no intermediates, and s is not reflexive""")
    reflexive_transitive_form_of: Optional[str] = Field(None, description="""transitive_form_of including the reflexive case""")
    role: Optional[str] = Field(None, description="""a textual descriptor that indicates the role played by the slot range""")
    is_usage_slot: Optional[bool] = Field(None, description="""True means that this slot was defined in a slot_usage situation""")
    usage_slot_name: Optional[str] = Field(None, description="""The name of the slot referenced in the slot_usage""")
    relational_role: Optional[RelationalRoleEnum] = Field(None, description="""the role a slot on a relationship class plays, for example, the subject, object or predicate roles""")
    slot_group: Optional[str] = Field(None, description="""allows for grouping of related slots into a grouping slot that serves the role of a group""")
    is_grouping_slot: Optional[bool] = Field(None, description="""true if this slot is a grouping slot""")
    path_rule: Optional[PathExpression] = Field(None, description="""a rule for inferring a slot assignment based on evaluating a path through a sequence of slot assignemnts""")
    disjoint_with: Optional[List[str]] = Field(default_factory=list, description="""Two classes are disjoint if they have no instances in common, two slots are disjoint if they can never hold between the same two instances""")
    children_are_mutually_disjoint: Optional[bool] = Field(None, description="""If true then all direct is_a children are mutually disjoint and share no instances in common""")
    union_of: Optional[List[str]] = Field(default_factory=list, description="""indicates that the domain element consists exactly of the members of the element in the range.""")
    range: Optional[str] = Field(None, description="""defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2
""")
    range_expression: Optional[AnonymousClassExpression] = Field(None, description="""A range that is described as a boolean expression combining existing ranges""")
    enum_range: Optional[EnumExpression] = Field(None, description="""An inlined enumeration""")
    required: Optional[bool] = Field(None, description="""true means that the slot must be present in the loaded definition""")
    recommended: Optional[bool] = Field(None, description="""true means that the slot should be present in the loaded definition, but this is not required""")
    inlined: Optional[bool] = Field(None, description="""True means that keyed or identified slot appears in an outer structure by value.  False means that only the key or identifier for the slot appears within the domain, referencing a structure that appears elsewhere.""")
    inlined_as_list: Optional[bool] = Field(None, description="""True means that an inlined slot is represented as a list of range instances.  False means that an inlined slot is represented as a dictionary, whose key is the slot key or identifier and whose value is the range instance.""")
    minimum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or higher than this""")
    maximum_value: Optional[int] = Field(None, description="""for slots with ranges of type number, the value must be equal to or lowe than this""")
    pattern: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string""")
    structured_pattern: Optional[PatternExpression] = Field(None, description="""the string value of the slot must conform to the regular expression in the pattern expression""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    implicit_prefix: Optional[str] = Field(None, description="""Causes the slot value to be interpreted as a uriorcurie after prefixing with this string""")
    value_presence: Optional[PresenceEnum] = Field(None, description="""if true then a value must be present (for lists there must be at least one value). If false then a value must be absent (for lists, must be empty)""")
    equals_string: Optional[str] = Field(None, description="""the slot must have range string and the value of the slot must equal the specified value""")
    equals_string_in: Optional[List[str]] = Field(default_factory=list, description="""the slot must have range string and the value of the slot must equal one of the specified values""")
    equals_number: Optional[int] = Field(None, description="""the slot must have range of a number and the value of the slot must equal the specified value""")
    equals_expression: Optional[str] = Field(None, description="""the value of the slot must equal the value of the evaluated expression""")
    minimum_cardinality: Optional[int] = Field(None, description="""the minimum number of entries for a multivalued slot""")
    maximum_cardinality: Optional[int] = Field(None, description="""the maximum number of entries for a multivalued slot""")
    has_member: Optional[AnonymousSlotExpression] = Field(None, description="""the value of the slot is multivalued with at least one member satisfying the condition""")
    all_members: Optional[AnonymousSlotExpression] = Field(None, description="""the value of the slot is multivalued with all members satisfying the condition""")
    none_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    any_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    all_of: Optional[List[AnonymousSlotExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    is_a: Optional[str] = Field(None, description="""A primary parent slot from which inheritable metaslots are propagated""")
    abstract: Optional[bool] = Field(None, description="""Indicates the class or slot cannot be directly instantiated and is intended for grouping and specifying core inherited metaslots""")
    mixin: Optional[bool] = Field(None, description="""Indicates the class or slot is intended to be inherited from without being an is_a parent. mixins should not be inherited from using is_a, except by other mixins.""")
    mixins: Optional[List[str]] = Field(default_factory=list, description="""A collection of secondary parent mixin slots from which inheritable metaslots are propagated""")
    apply_to: Optional[List[str]] = Field(default_factory=list, description="""Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.""")
    values_from: Optional[List[str]] = Field(default_factory=list, description="""The identifier of a \"value set\" -- a set of identifiers that form the possible values for the range of a slot. Note: this is different than 'subproperty_of' in that 'subproperty_of' is intended to be a single ontology term while 'values_from' is the identifier of an entire value set.  Additionally, this is different than an enumeration in that in an enumeration, the values of the enumeration are listed directly in the model itself. Setting this property on a slot does not guarantee an expansion of the ontological hiearchy into an enumerated list of possible values in every serialization of the model.""")
    created_by: Optional[str] = Field(None, description="""agent that created the element""")
    created_on: Optional[datetime ] = Field(None, description="""time at which the element was created""")
    last_updated_on: Optional[datetime ] = Field(None, description="""time at which the element was last updated""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    status: Optional[str] = Field(None, description="""status of the element""")
    string_serialization: Optional[str] = Field(None, description="""Used on a slot that stores the string serialization of the containing object. The syntax follows python formatted strings, with slot names enclosed in {}s. These are expanded using the values of those slots.
We call the slot with the serialization the s-slot, the slots used in the {}s are v-slots. If both s-slots and v-slots are populated on an object then the value of the s-slot should correspond to the expansion.
Implementations of frameworks may choose to use this property to either (a) PARSE: implement automated normalizations by parsing denormalized strings into complex objects (b) GENERARE: implement automated to_string labeling of complex objects
For example, a Measurement class may have 3 fields: unit, value, and string_value. The string_value slot may have a string_serialization of {value}{unit} such that if unit=cm and value=2, the value of string_value shouldd be 2cm""")
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class AnonymousClassExpression(AnonymousExpression, ClassExpression):
    
    is_a: Optional[str] = Field(None, description="""A primary parent class or slot from which inheritable metaslots are propagated from. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded""")
    any_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    none_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    all_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    slot_conditions: Optional[Dict[str, SlotDefinition]] = Field(default_factory=dict, description="""expresses constraints on a group of slots for a class expression""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class ClassDefinition(Definition, ClassExpression):
    """
    an element whose instances are complex objects that may have slot-value assignments
    """
    slots: Optional[List[str]] = Field(default_factory=list, description="""collection of slot names that are applicable to a class""")
    slot_usage: Optional[Dict[str, SlotDefinition]] = Field(default_factory=dict, description="""the refinement of a slot in the context of the containing class definition.""")
    attributes: Optional[Dict[str, SlotDefinition]] = Field(default_factory=dict, description="""Inline definition of slots""")
    class_uri: Optional[str] = Field(None, description="""URI of the class that provides a semantic interpretation of the element in a linked data context. The URI may come from any namespace and may be shared between schemas""")
    subclass_of: Optional[str] = Field(None, description="""rdfs:subClassOf to be emitted in OWL generation""")
    union_of: Optional[List[str]] = Field(default_factory=list, description="""indicates that the domain element consists exactly of the members of the element in the range.""")
    defining_slots: Optional[List[str]] = Field(default_factory=list, description="""The combination of is a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom""")
    tree_root: Optional[bool] = Field(None, description="""indicator that this is the root class in tree structures""")
    unique_keys: Optional[List[UniqueKey]] = Field(default_factory=list, description="""A collection of unique keys for this class. Unique keys may be singular or compound.""")
    rules: Optional[List[ClassRule]] = Field(default_factory=list, description="""the collection of rules that apply to all members of this class""")
    classification_rules: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""the collection of classification rules that apply to all members of this class""")
    slot_names_unique: Optional[bool] = Field(None, description="""if true then induced/mangled slot names are not created for class_usage and attributes""")
    represents_relationship: Optional[bool] = Field(None, description="""true if this class represents a relationship rather than an entity""")
    disjoint_with: Optional[List[str]] = Field(default_factory=list, description="""Two classes are disjoint if they have no instances in common, two slots are disjoint if they can never hold between the same two instances""")
    children_are_mutually_disjoint: Optional[bool] = Field(None, description="""If true then all direct is_a children are mutually disjoint and share no instances in common""")
    any_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if at least one of the expressions hold""")
    exactly_one_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if only one of the expressions hold""")
    none_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if none of the expressions hold""")
    all_of: Optional[List[AnonymousClassExpression]] = Field(default_factory=list, description="""holds if all of the expressions hold""")
    slot_conditions: Optional[Dict[str, SlotDefinition]] = Field(default_factory=dict, description="""expresses constraints on a group of slots for a class expression""")
    is_a: Optional[str] = Field(None, description="""A primary parent class from which inheritable metaslots are propagated""")
    abstract: Optional[bool] = Field(None, description="""Indicates the class or slot cannot be directly instantiated and is intended for grouping and specifying core inherited metaslots""")
    mixin: Optional[bool] = Field(None, description="""Indicates the class or slot is intended to be inherited from without being an is_a parent. mixins should not be inherited from using is_a, except by other mixins.""")
    mixins: Optional[List[str]] = Field(default_factory=list, description="""A collection of secondary parent mixin classes from which inheritable metaslots are propagated""")
    apply_to: Optional[List[str]] = Field(default_factory=list, description="""Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.""")
    values_from: Optional[List[str]] = Field(default_factory=list, description="""The identifier of a \"value set\" -- a set of identifiers that form the possible values for the range of a slot. Note: this is different than 'subproperty_of' in that 'subproperty_of' is intended to be a single ontology term while 'values_from' is the identifier of an entire value set.  Additionally, this is different than an enumeration in that in an enumeration, the values of the enumeration are listed directly in the model itself. Setting this property on a slot does not guarantee an expansion of the ontological hiearchy into an enumerated list of possible values in every serialization of the model.""")
    created_by: Optional[str] = Field(None, description="""agent that created the element""")
    created_on: Optional[datetime ] = Field(None, description="""time at which the element was created""")
    last_updated_on: Optional[datetime ] = Field(None, description="""time at which the element was last updated""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    status: Optional[str] = Field(None, description="""status of the element""")
    string_serialization: Optional[str] = Field(None, description="""Used on a slot that stores the string serialization of the containing object. The syntax follows python formatted strings, with slot names enclosed in {}s. These are expanded using the values of those slots.
We call the slot with the serialization the s-slot, the slots used in the {}s are v-slots. If both s-slots and v-slots are populated on an object then the value of the s-slot should correspond to the expansion.
Implementations of frameworks may choose to use this property to either (a) PARSE: implement automated normalizations by parsing denormalized strings into complex objects (b) GENERARE: implement automated to_string labeling of complex objects
For example, a Measurement class may have 3 fields: unit, value, and string_value. The string_value slot may have a string_serialization of {value}{unit} such that if unit=cm and value=2, the value of string_value shouldd be 2cm""")
    name: Optional[str] = Field(None, description="""the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.""")
    id_prefixes: Optional[List[str]] = Field(default_factory=list, description="""the identifier of this class or slot must begin with the URIs referenced by this prefix""")
    definition_uri: Optional[str] = Field(None, description="""the \"native\" URI of the element""")
    local_names: Optional[List[LocalName]] = Field(default_factory=list)
    conforms_to: Optional[str] = Field(None, description="""An established standard to which the element conforms.""")
    implements: Optional[List[str]] = Field(default_factory=list, description="""An element in another schema which this element conforms to""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class ClassRule(Extensible, Annotatable, ClassLevelRule, CommonMetadata):
    """
    A rule that applies to instances of a class
    """
    preconditions: Optional[AnonymousClassExpression] = Field(None, description="""an expression that must hold in order for the rule to be applicable to an instance""")
    postconditions: Optional[AnonymousClassExpression] = Field(None, description="""an expression that must hold for an instance of the class, if the preconditions hold""")
    elseconditions: Optional[AnonymousClassExpression] = Field(None, description="""an expression that must hold for an instance of the class, if the preconditions no not hold""")
    bidirectional: Optional[bool] = Field(None, description="""in addition to preconditions entailing postconditions, the postconditions entail the preconditions""")
    open_world: Optional[bool] = Field(None, description="""if true, the the postconditions may be omitted in instance data, but it is valid for an inference engine to add these""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    deactivated: Optional[bool] = Field(None, description="""a deactivated rule is not executed by the rules engine""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    


class PatternExpression(Extensible, Annotatable, CommonMetadata):
    """
    a regular expression pattern used to evaluate conformance of a string
    """
    syntax: Optional[str] = Field(None, description="""the string value of the slot must conform to this regular expression expressed in the string. May be interpolated.""")
    interpolated: Optional[bool] = Field(None, description="""if true then the pattern is first string interpolated""")
    partial_match: Optional[bool] = Field(None, description="""if true then the pattern must match the whole string, as if enclosed in ^...$""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class ImportExpression(Extensible, Annotatable, CommonMetadata):
    """
    an expression describing an import
    """
    import_from: str = Field(None)
    import_as: Optional[str] = Field(None)
    import_map: Optional[List[Setting]] = Field(default_factory=list)
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class PermissibleValue(Extensible, Annotatable, CommonMetadata):
    """
    a permissible value, accompanied by intended text and an optional mapping to a concept URI
    """
    text: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    meaning: Optional[str] = Field(None, description="""the value meaning of a permissible value""")
    unit: Optional[UnitOfMeasure] = Field(None, description="""an encoding of a unit""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    


class UniqueKey(Extensible, Annotatable, CommonMetadata):
    """
    a collection of slots whose values uniquely identify an instance of a class
    """
    unique_key_name: str = Field(None, description="""name of the unique key""")
    unique_key_slots: List[str] = Field(default_factory=list, description="""list of slot names that form a key""")
    extensions: Optional[List[Extension]] = Field(default_factory=list, description="""a tag/text tuple attached to an arbitrary element""")
    annotations: Optional[List[Annotation]] = Field(default_factory=list, description="""a collection of tag/text tuples with the semantics of OWL Annotation""")
    description: Optional[str] = Field(None, description="""a description of the element's purpose and use""")
    alt_descriptions: Optional[List[AltDescription]] = Field(default_factory=list, description="""A sourced alternative description for an element""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    deprecated: Optional[str] = Field(None, description="""Description of why and when this element will no longer be used""")
    todos: Optional[List[str]] = Field(default_factory=list, description="""Outstanding issue that needs resolution""")
    notes: Optional[List[str]] = Field(default_factory=list, description="""editorial notes about an element intended for internal consumption""")
    comments: Optional[List[str]] = Field(default_factory=list, description="""notes and comments about an element intended for external consumption""")
    examples: Optional[List[Example]] = Field(default_factory=list, description="""example usages of an element""")
    in_subset: Optional[List[str]] = Field(default_factory=list, description="""used to indicate membership of a term in a defined subset of terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)""")
    from_schema: Optional[str] = Field(None, description="""id of the schema that defined the element""")
    imported_from: Optional[str] = Field(None, description="""the imports entry that this element was derived from.  Empty means primary source""")
    source: Optional[str] = Field(None, description="""A related resource from which the element is derived.""")
    in_language: Optional[str] = Field(None)
    see_also: Optional[List[str]] = Field(default_factory=list, description="""a reference""")
    deprecated_element_has_exact_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be automatically replaced by this uri or curie""")
    deprecated_element_has_possible_replacement: Optional[str] = Field(None, description="""When an element is deprecated, it can be potentially replaced by this uri or curie""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alaternate names for the element""")
    structured_aliases: Optional[List[StructuredAlias]] = Field(default_factory=list, description="""A list of structured_alias objects.""")
    mappings: Optional[List[str]] = Field(default_factory=list, description="""A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.""")
    exact_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""")
    close_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have close meaning.""")
    related_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have related meaning.""")
    narrow_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""")
    broad_mappings: Optional[List[str]] = Field(None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""")
    rank: Optional[int] = Field(None, description="""the relative order in which the element occurs, lower values are given precedence""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
CodeableConcept.update_forward_refs()
Variable.update_forward_refs()
UnitLevelVariable.update_forward_refs()
VariableRelationship.update_forward_refs()
VariableCollection.update_forward_refs()
QuantityType.update_forward_refs()
PhysicalEntityOrPhenomena.update_forward_refs()
PhysicalEntity.update_forward_refs()
PhysicalSubstance.update_forward_refs()
Measurable.update_forward_refs()
MeasurementContext.update_forward_refs()
Device.update_forward_refs()
ValueDomain.update_forward_refs()
StructuredMapping.update_forward_refs()
CommonMetadata.update_forward_refs()
MatchQuery.update_forward_refs()
ReachabilityQuery.update_forward_refs()
Expression.update_forward_refs()
TypeExpression.update_forward_refs()
AnonymousTypeExpression.update_forward_refs()
EnumExpression.update_forward_refs()
AnonymousEnumExpression.update_forward_refs()
SlotExpression.update_forward_refs()
ClassExpression.update_forward_refs()
ClassLevelRule.update_forward_refs()
Setting.update_forward_refs()
Prefix.update_forward_refs()
LocalName.update_forward_refs()
Example.update_forward_refs()
AltDescription.update_forward_refs()
UnitOfMeasure.update_forward_refs()
Annotatable.update_forward_refs()
Extension.update_forward_refs()
Annotation.update_forward_refs()
Extensible.update_forward_refs()
Element.update_forward_refs()
SchemaDefinition.update_forward_refs()
TypeDefinition.update_forward_refs()
SubsetDefinition.update_forward_refs()
Definition.update_forward_refs()
EnumDefinition.update_forward_refs()
StructuredAlias.update_forward_refs()
AnonymousExpression.update_forward_refs()
PathExpression.update_forward_refs()
AnonymousSlotExpression.update_forward_refs()
SlotDefinition.update_forward_refs()
AnonymousClassExpression.update_forward_refs()
ClassDefinition.update_forward_refs()
ClassRule.update_forward_refs()
PatternExpression.update_forward_refs()
ImportExpression.update_forward_refs()
PermissibleValue.update_forward_refs()
UniqueKey.update_forward_refs()

