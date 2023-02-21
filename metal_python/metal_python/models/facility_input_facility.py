# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from typing import Any, List
from pydantic import StrictStr, Field

FACILITYINPUTFACILITY_ANY_OF_SCHEMAS = ["List[str]", "str"]

class FacilityInputFacility(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: List[str]
    anyof_schema_1_validator: Optional[List[StrictStr]] = None
    # data type: str
    anyof_schema_2_validator: Optional[StrictStr] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(FACILITYINPUTFACILITY_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = cls()
        error_messages = []
        # validate data type: List[str]
        try:
            instance.anyof_schema_1_validator = v
            return v
        except ValidationError as e:
            error_messages.append(str(e))
        # validate data type: str
        try:
            instance.anyof_schema_2_validator = v
            return v
        except ValidationError as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FacilityInputFacility with anyOf schemas: List[str], str. Details: " + ", ".join(error_messages))
        else:
            return v
    @classmethod
    def from_dict(cls, obj: dict) -> FacilityInputFacility:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> FacilityInputFacility:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        # deserialize data into List[str]
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except ValidationError as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FacilityInputFacility with anyOf schemas: List[str], str. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

