from __future__ import annotations

import re
import sys
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


metamodel_version = "None"
version = "0.0.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_curi_maps": ["semweb_context"],
        "default_prefix": "https://ibm.github.io/risk-atlas-nexus/ontology/ares/",
        "default_range": "string",
        "description": "Vocabulary to integrate Ares workflow",
        "id": "https://ibm.github.io/risk-atlas-nexus/ontology/ares",
        "imports": ["linkml:types", "common"],
        "name": "ares",
        "prefixes": {
            "linkml": {
                "prefix_prefix": "linkml",
                "prefix_reference": "https://w3id.org/linkml/",
            }
        },
        "source_file": "schema.yaml",
    }
)


class Entity(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "schema:Thing",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common",
        }
    )

    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class Organization(Entity):
    """
    Any organizational entity such as a corporation, educational institution, consortium, government, etc.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:Organization",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common",
        }
    )

    grants_license: Optional[str] = Field(
        default=None,
        description="""A relationship from a granting entity such as an Organization to a License instance.""",
        json_schema_extra={
            "linkml_meta": {"alias": "grants_license", "domain_of": ["Organization"]}
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class License(Entity):
    """
    The general notion of a license which defines terms and grants permissions to users of AI systems, datasets and software.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "airo:License",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common",
        }
    )

    version: Optional[str] = Field(
        default=None,
        description="""The version of the entity embodied by a specified resource.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["License", "Vocabulary"],
                "slot_uri": "schema:version",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class Dataset(Entity):
    """
    A body of structured information describing some topic(s) of interest.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:Dataset",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common",
        }
    )

    hasLicense: Optional[str] = Field(
        default=None,
        description="""Indicates licenses associated with a resource""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasLicense",
                "domain_of": ["Dataset", "Documentation", "Vocabulary"],
                "slot_uri": "airo:hasLicense",
            }
        },
    )
    hasDocumentation: Optional[list[str]] = Field(
        default=None,
        description="""Indicates documentation associated with an entity.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasDocumentation",
                "domain_of": ["Dataset", "Vocabulary", "Term"],
                "slot_uri": "airo:hasDocumentation",
            }
        },
    )
    provider: Optional[str] = Field(
        default=None,
        description="""A relationship to the Organization instance that provides this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "provider",
                "domain_of": ["Dataset"],
                "slot_uri": "schema:provider",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class Documentation(Entity):
    """
    Documented information about a concept or other topic(s) of interest.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "airo:Documentation",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common",
        }
    )

    hasLicense: Optional[str] = Field(
        default=None,
        description="""Indicates licenses associated with a resource""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasLicense",
                "domain_of": ["Dataset", "Documentation", "Vocabulary"],
                "slot_uri": "airo:hasLicense",
            }
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""The author or authors of the documentation""",
        json_schema_extra={
            "linkml_meta": {"alias": "author", "domain_of": ["Documentation"]}
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class Fact(ConfiguredBaseModel):
    """
    A fact about something, for example the result of a measurement. In addition to the value, evidence is provided.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "schema:Statement",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common",
        }
    )

    value: str = Field(
        default=...,
        description="""Some numeric or string value""",
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Fact"]}},
    )
    evidence: Optional[str] = Field(
        default=None,
        description="""Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated.""",
        json_schema_extra={"linkml_meta": {"alias": "evidence", "domain_of": ["Fact"]}},
    )


class Vocabulary(Entity):
    """
    A collection of terms, with their definitions and relationships.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common"}
    )

    version: Optional[str] = Field(
        default=None,
        description="""The version of the entity embodied by a specified resource.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["License", "Vocabulary"],
                "slot_uri": "schema:version",
            }
        },
    )
    hasDocumentation: Optional[list[str]] = Field(
        default=None,
        description="""Indicates documentation associated with an entity.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasDocumentation",
                "domain_of": ["Dataset", "Vocabulary", "Term"],
                "slot_uri": "airo:hasDocumentation",
            }
        },
    )
    hasLicense: Optional[str] = Field(
        default=None,
        description="""Indicates licenses associated with a resource""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasLicense",
                "domain_of": ["Dataset", "Documentation", "Vocabulary"],
                "slot_uri": "airo:hasLicense",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class Term(Entity):
    """
    A term and its definitions
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/common"}
    )

    isDefinedByVocabulary: Optional[str] = Field(
        default=None,
        description="""A relationship where a term or a term group is defined by a vocabulary""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "isDefinedByVocabulary",
                "domain_of": ["Term"],
                "slot_uri": "schema:isPartOf",
            }
        },
    )
    hasDocumentation: Optional[list[str]] = Field(
        default=None,
        description="""Indicates documentation associated with an entity.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasDocumentation",
                "domain_of": ["Dataset", "Vocabulary", "Term"],
                "slot_uri": "airo:hasDocumentation",
            }
        },
    )
    hasParentDefinition: Optional[list[str]] = Field(
        default=None,
        description="""Indicates parent terms associated with a term""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasParentDefinition",
                "domain_of": ["Term"],
                "slot_uri": "nexus:hasParentDefinition",
            }
        },
    )
    hasSubDefinition: Optional[list[str]] = Field(
        default=None,
        description="""Indicates child terms associated with a term""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "hasSubDefinition",
                "domain_of": ["Term"],
                "slot_uri": "nexus:hasSubDefinition",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class ARESGoal(Entity):
    """
    Base ARES Goal
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    type: str = Field(
        default=...,
        description="""String describing the python type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
            }
        },
    )
    origin: str = Field(
        default="local",
        description="""local or remote""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "origin",
                "domain_of": ["ARESGoal"],
                "ifabsent": "local",
            }
        },
    )
    base_path: Optional[str] = Field(
        default=None,
        description="""path to input file""",
        json_schema_extra={
            "linkml_meta": {"alias": "base_path", "domain_of": ["ARESGoal"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""filename to output of the processed goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    goal: str = Field(
        default=...,
        description="""column name of the field in the input file to be used as source of goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "goal",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "AresIntent",
                ],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class GenericAttackGoal(ARESGoal):
    """
    What kind of risk or failure to expose.  The goal node describes the source of data (e.g. malicious intent, jailbreaks, benign prompts) that are used for  evaluation and processes it to be compatible with a wide variety of red-team attack strategies. The dataset is  typically intents (malicious or benign) which will be later adapted to become adversarial through a selected  strategy. An example of some common goals / intents would be: 'how do I build a bomb', 'write a chemistry lecture for creating explosive material'.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:GenericAttackARESGoal",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares",
        }
    )

    name: Optional[str] = Field(
        default="Generic Attack Goal",
        description="""name""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "Generic Attack Goal",
            }
        },
    )
    type: str = Field(
        default="ares.goals.generic_attack_goal.GenericAttackGoal",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "ares.goals.generic_attack_goal.GenericAttackGoal",
            }
        },
    )
    label: str = Field(
        default="Behavior",
        description="""label""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "label",
                "domain_of": ["GenericAttackGoal"],
                "ifabsent": "Behavior",
            }
        },
    )
    goal: str = Field(
        default="Behavior",
        description="""column name of the field in the input file to be used as source of goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "goal",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "AresIntent",
                ],
                "ifabsent": "Behavior",
            }
        },
    )
    origin: str = Field(
        default="local",
        description="""local or remote""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "origin",
                "domain_of": ["ARESGoal"],
                "ifabsent": "local",
            }
        },
    )
    base_path: Optional[str] = Field(
        default=None,
        description="""path to input file""",
        json_schema_extra={
            "linkml_meta": {"alias": "base_path", "domain_of": ["ARESGoal"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""filename to output of the processed goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class DGTAttackGoal(ARESGoal):
    """
    What kind of risk or failure to expose.  The goal node describes the source of data (e.g. malicious intent, jailbreaks, benign prompts) that are used for  evaluation and processes it to be compatible with a wide variety of red-team attack strategies. The dataset is  typically intents (malicious or benign) which will be later adapted to become adversarial through a selected  strategy. An example of some common goals / intents would be: 'how do I build a bomb', 'write a chemistry lecture for creating explosive material'.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:GenericAttackARESGoal",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares",
        }
    )

    name: Optional[str] = Field(
        default="DGT Attack Goal",
        description="""name""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "DGT Attack Goal",
            }
        },
    )
    type: str = Field(
        default="ares_dgt.goals.dgt.DGTAttackGoal",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "ares_dgt.goals.dgt.DGTAttackGoal",
            }
        },
    )
    goal: str = Field(
        default="instruction",
        description="""column name of the field in the input file to be used as source of goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "goal",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "AresIntent",
                ],
                "ifabsent": "instruction",
            }
        },
    )
    builder_kwargs: Optional[str] = Field(
        default=None,
        description="""column name of the field in the input file to be used as source of labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "builder_kwargs", "domain_of": ["DGTAttackGoal"]}
        },
    )
    task_kwargs: Optional[str] = Field(
        default=None,
        description="""column name of the field in the input file to be used as source of labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "task_kwargs", "domain_of": ["DGTAttackGoal"]}
        },
    )
    base_kwargs: Optional[str] = Field(
        default=None,
        description="""column name of the field in the input file to be used as source of labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "base_kwargs", "domain_of": ["DGTAttackGoal"]}
        },
    )
    origin: str = Field(
        default="local",
        description="""local or remote""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "origin",
                "domain_of": ["ARESGoal"],
                "ifabsent": "local",
            }
        },
    )
    base_path: Optional[str] = Field(
        default=None,
        description="""path to input file""",
        json_schema_extra={
            "linkml_meta": {"alias": "base_path", "domain_of": ["ARESGoal"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""filename to output of the processed goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class ARESStrategy(Entity):
    """
    The type of attacks or evaluation techniques.  The strategy used for red-teaming the language model and, in  particular, for transforming the goal prompts saved in the previous step to adversarial attack prompts.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    type: str = Field(
        default=...,
        description="""String describing the python type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
            }
        },
    )
    input_path: str = Field(
        default=...,
        description="""The input path""",
        json_schema_extra={
            "linkml_meta": {"alias": "input_path", "domain_of": ["ARESStrategy"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""The output path""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class HumanJailbreak(ARESStrategy):
    """
    The type of attacks or evaluation techniques.  The strategy used for red-teaming the language model and, in  particular, for transforming the goal prompts saved in the previous step to adversarial attack prompts.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    name: Optional[str] = Field(
        default="human_jailbreak",
        description="""name""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "human_jailbreak",
            }
        },
    )
    type: str = Field(
        default="ares_human_jailbreak.strategies.human_jailbreak.HumanJailbreak",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "ares_human_jailbreak.strategies.human_jailbreak.HumanJailbreak",
            }
        },
    )
    jailbreaks_path: str = Field(
        default=...,
        description="""String describing the python type""",
        json_schema_extra={
            "linkml_meta": {"alias": "jailbreaks_path", "domain_of": ["HumanJailbreak"]}
        },
    )
    input_path: str = Field(
        default=...,
        description="""The input path""",
        json_schema_extra={
            "linkml_meta": {"alias": "input_path", "domain_of": ["ARESStrategy"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""The output path""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class DirectRequests(ARESStrategy):
    """
    The type of attacks or evaluation techniques.  The strategy used for red-teaming the language model and, in  particular, for transforming the goal prompts saved in the previous step to adversarial attack prompts.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    name: Optional[str] = Field(
        default="direct_requests",
        description="""name""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "direct_requests",
            }
        },
    )
    type: str = Field(
        default="ares.strategies.direct_requests.DirectRequests",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "ares.strategies.direct_requests.DirectRequests",
            }
        },
    )
    input_path: str = Field(
        default=...,
        description="""The input path""",
        json_schema_extra={
            "linkml_meta": {"alias": "input_path", "domain_of": ["ARESStrategy"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""The output path""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class InjectASCII(ARESStrategy):
    """
    The type of attacks or evaluation techniques.  The strategy used for red-teaming the language model and, in  particular, for transforming the goal prompts saved in the previous step to adversarial attack prompts.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    name: Optional[str] = Field(
        default="probes.encoding.InjectROT13",
        description="""name""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "probes.encoding.InjectROT13",
            }
        },
    )
    type: str = Field(
        default="ares_garak.strategies.encoding.EncodingStrategy",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "ares_garak.strategies.encoding.EncodingStrategy",
            }
        },
    )
    probe: str = Field(
        default=...,
        description="""String describing the probe type""",
        json_schema_extra={
            "linkml_meta": {"alias": "probe", "domain_of": ["InjectASCII"]}
        },
    )
    templates: Optional[str] = Field(
        default=None,
        description="""String describing the python type""",
        json_schema_extra={
            "linkml_meta": {"alias": "templates", "domain_of": ["InjectASCII"]}
        },
    )
    input_path: str = Field(
        default=...,
        description="""The input path""",
        json_schema_extra={
            "linkml_meta": {"alias": "input_path", "domain_of": ["ARESStrategy"]}
        },
    )
    output_path: str = Field(
        default=...,
        description="""The output path""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class AresEvaluator(Entity):
    """
    How to measure and report results. The evaluation node describes the evaluators assessing the performance of the  target LM under attack.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    type: str = Field(
        default=...,
        description="""String describing the python type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
            }
        },
    )
    output_path: str = Field(
        default="results/evaluation.json",
        description="""The output path for the evaluation results""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
                "ifabsent": "results/evaluation.json",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class READIEvaluator(AresEvaluator):
    """
    How to measure and report results. The evaluation node describes the evaluators assessing the performance of the  target LM under attack.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    name: Optional[str] = Field(
        default="READIEvaluator",
        description="""name""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "READIEvaluator",
            }
        },
    )
    type: str = Field(
        default="readi_eval.READIEvaluator",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "readi_eval.READIEvaluator",
            }
        },
    )
    sensitive_type: Optional[str] = Field(
        default=None,
        description="""String describing the ARES evaluation type""",
        json_schema_extra={
            "linkml_meta": {"alias": "sensitive_type", "domain_of": ["READIEvaluator"]}
        },
    )
    exclude_prompt: Optional[bool] = Field(
        default=None,
        description="""The input path the path to dataset of attacks generated by strategy""",
        json_schema_extra={
            "linkml_meta": {"alias": "exclude_prompt", "domain_of": ["READIEvaluator"]}
        },
    )
    debug_mode: Optional[bool] = Field(
        default=None,
        description="""The output path for the evaluation results""",
        json_schema_extra={
            "linkml_meta": {"alias": "debug_mode", "domain_of": ["READIEvaluator"]}
        },
    )
    output_path: str = Field(
        default="results/evaluation.json",
        description="""The output path for the evaluation results""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
                "ifabsent": "results/evaluation.json",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class KeywordEvaluator(AresEvaluator):
    """
    How to measure and report results. The evaluation node describes the evaluators assessing the performance of the  target LM under attack.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    name: Optional[str] = Field(
        default="keyword",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "ifabsent": "KeywordEvaluator",
            }
        },
    )
    type: str = Field(
        default="ares.evals.keyword_eval.KeywordEval",
        description="""type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
                "ifabsent": "ares.evals.keyword_eval.KeywordEval",
            }
        },
    )
    keyword_list_or_path: str = Field(
        default="assets/advbench_refusal_keywords.json",
        description="""String describing the ARES evaluation type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "keyword_list_or_path",
                "domain_of": ["KeywordEvaluator"],
                "ifabsent": "assets/advbench_refusal_keywords.json",
            }
        },
    )
    output_path: str = Field(
        default="results/evaluation.json",
        description="""The output path for the evaluation results""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "output_path",
                "domain_of": ["ARESGoal", "ARESStrategy", "AresEvaluator"],
                "ifabsent": "results/evaluation.json",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class AresIntent(Entity):
    """
    An ARES intent
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:AresIntent",
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares",
        }
    )

    goal: Union[DGTAttackGoal, GenericAttackGoal] = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "goal",
                "any_of": [{"range": "GenericAttackGoal"}, {"range": "DGTAttackGoal"}],
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "AresIntent",
                ],
            }
        },
    )
    strategy: dict[str, Union[DirectRequests, HumanJailbreak, InjectASCII]] = Field(
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strategy",
                "any_of": [
                    {"range": "DirectRequests"},
                    {"range": "HumanJailbreak"},
                    {"range": "InjectASCII"},
                ],
                "domain_of": ["AresIntent"],
            }
        },
    )
    evaluation: Union[KeywordEvaluator, READIEvaluator] = Field(
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "evaluation",
                "any_of": [{"range": "READIEvaluator"}, {"range": "KeywordEvaluator"}],
                "domain_of": ["AresIntent"],
            }
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class RedTeaming(Entity):
    """
    ARES uses intents to configure red-teaming.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    intent: str = Field(
        default=...,
        description="""intent name""",
        json_schema_extra={
            "linkml_meta": {"alias": "intent", "domain_of": ["RedTeaming"]}
        },
    )
    intent_config: dict[str, AresIntent] = Field(
        default=...,
        description="""intent instance""",
        json_schema_extra={
            "linkml_meta": {"alias": "intent_config", "domain_of": ["RedTeaming"]}
        },
    )
    prompts: str = Field(
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {"alias": "prompts", "domain_of": ["RedTeaming"]}
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class ARESConfig(Entity):
    """
    ARES uses intents to configure red-teaming.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    target: dict[str, Connector] = Field(
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {"alias": "target", "domain_of": ["ARESConfig"]}
        },
    )
    red_teaming: RedTeaming = Field(
        serialization_alias="red-teaming",
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {"alias": "red-teaming", "domain_of": ["ARESConfig"]}
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class RiskGroupToARESConfig(Entity):
    """
    ARES uses intents to configure red-teaming.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    risk_attack_id: str = Field(
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "risk_attack_id",
                "domain_of": ["RiskGroupToARESConfig"],
            }
        },
    )
    config: ARESConfig = Field(
        default=...,
        description="""The path to the prompts file""",
        json_schema_extra={
            "linkml_meta": {"alias": "config", "domain_of": ["RiskGroupToARESConfig"]}
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class RiskGroupToARESConfigList(ConfiguredBaseModel):
    """
    An umbrella object that holds the ontology class instances
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares",
            "tree_root": True,
        }
    )

    mappings: Optional[list[RiskGroupToARESConfig]] = Field(
        default=None,
        description="""A list of ares goals""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "mappings",
                "domain_of": ["RiskGroupToARESConfigList"],
            }
        },
    )


class Connector(Entity):
    """
    An ARES intent
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    type: str = Field(
        default=...,
        description="""String describing the python type""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": [
                    "ARESGoal",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "ARESStrategy",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "AresEvaluator",
                    "READIEvaluator",
                    "KeywordEvaluator",
                    "Connector",
                ],
            }
        },
    )
    seed: Optional[int] = Field(
        default=None,
        description="""Seed to be applied to model, for example, 42.""",
        json_schema_extra={
            "linkml_meta": {"alias": "seed", "domain_of": ["Connector"]}
        },
    )
    device: Optional[str] = Field(
        default="auto",
        description="""Device on which to load the model, for example, 'auto'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "device",
                "domain_of": ["Connector"],
                "ifabsent": "auto",
            }
        },
    )
    model_configs: Optional[ModelConfig] = Field(
        serialization_alias="model_config",
        default=None,
        description="""model_config""",
        json_schema_extra={
            "linkml_meta": {"alias": "model_configs", "domain_of": ["Connector"]}
        },
    )
    tokenizer_config: TokenizerConfig = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {"alias": "tokenizer_config", "domain_of": ["Connector"]}
        },
    )
    generate_kwargs: Optional[GenerateKwargs] = Field(
        default=None,
        description="""JSON schema for the config passed used for generate kwargs.""",
        json_schema_extra={
            "linkml_meta": {"alias": "generate_kwargs", "domain_of": ["Connector"]}
        },
    )
    id: str = Field(
        default=...,
        description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["Entity"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""A text name of this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": [
                    "Entity",
                    "GenericAttackGoal",
                    "DGTAttackGoal",
                    "HumanJailbreak",
                    "DirectRequests",
                    "InjectASCII",
                    "READIEvaluator",
                    "KeywordEvaluator",
                ],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""The description of an entity""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["Entity"],
                "slot_uri": "schema:description",
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""An optional URL associated with this instance.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "url",
                "domain_of": ["Entity"],
                "slot_uri": "schema:url",
            }
        },
    )
    dateCreated: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was created.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateCreated",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateCreated",
            }
        },
    )
    dateModified: Optional[date] = Field(
        default=None,
        description="""The date on which the entity was most recently modified.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "dateModified",
                "domain_of": ["Entity"],
                "slot_uri": "schema:dateModified",
            }
        },
    )


class ModelConfig(ConfiguredBaseModel):
    """
    An ARES intent
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    pretrained_model_name_or_path: str = Field(
        default=...,
        description="""pretrained_model_name_or_path""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "pretrained_model_name_or_path",
                "domain_of": ["ModelConfig", "TokenizerConfig"],
            }
        },
    )
    torch_dtype: Optional[str] = Field(
        default=None,
        description="""model_config""",
        json_schema_extra={
            "linkml_meta": {"alias": "torch_dtype", "domain_of": ["ModelConfig"]}
        },
    )


class TokenizerConfig(ConfiguredBaseModel):
    """
    Connector config
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    pretrained_model_name_or_path: str = Field(
        default=...,
        description="""pretrained_model_name_or_path""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "pretrained_model_name_or_path",
                "domain_of": ["ModelConfig", "TokenizerConfig"],
            }
        },
    )
    padding_side: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "padding_side", "domain_of": ["TokenizerConfig"]}
        },
    )


class GenerateKwargs(ConfiguredBaseModel):
    """
    Connector config
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    chat_template: Optional[ChatTemplate] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "chat_template", "domain_of": ["GenerateKwargs"]}
        },
    )
    generate_params: Optional[GenerateParams] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "generate_params", "domain_of": ["GenerateKwargs"]}
        },
    )


class ChatTemplate(ConfiguredBaseModel):
    """
    Connector config
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    return_tensors: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "return_tensors", "domain_of": ["ChatTemplate"]}
        },
    )
    thinking: Optional[bool] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "thinking", "domain_of": ["ChatTemplate"]}
        },
    )
    return_dict: Optional[bool] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "return_dict", "domain_of": ["ChatTemplate"]}
        },
    )
    add_generation_prompt: Optional[bool] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "add_generation_prompt",
                "domain_of": ["ChatTemplate"],
            }
        },
    )


class GenerateParams(ConfiguredBaseModel):
    """
    Connector config
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://ibm.github.io/risk-atlas-nexus/ontology/ares"}
    )

    max_new_tokens: Optional[int] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "max_new_tokens", "domain_of": ["GenerateParams"]}
        },
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Entity.model_rebuild()
Organization.model_rebuild()
License.model_rebuild()
Dataset.model_rebuild()
Documentation.model_rebuild()
Fact.model_rebuild()
Vocabulary.model_rebuild()
Term.model_rebuild()
ARESGoal.model_rebuild()
GenericAttackGoal.model_rebuild()
DGTAttackGoal.model_rebuild()
ARESStrategy.model_rebuild()
HumanJailbreak.model_rebuild()
DirectRequests.model_rebuild()
InjectASCII.model_rebuild()
AresEvaluator.model_rebuild()
READIEvaluator.model_rebuild()
KeywordEvaluator.model_rebuild()
AresIntent.model_rebuild()
RedTeaming.model_rebuild()
ARESConfig.model_rebuild()
RiskGroupToARESConfig.model_rebuild()
RiskGroupToARESConfigList.model_rebuild()
Connector.model_rebuild()
ModelConfig.model_rebuild()
TokenizerConfig.model_rebuild()
GenerateKwargs.model_rebuild()
ChatTemplate.model_rebuild()
GenerateParams.model_rebuild()
