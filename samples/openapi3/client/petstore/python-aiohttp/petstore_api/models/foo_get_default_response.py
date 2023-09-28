# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from petstore_api.models.foo import Foo

class FooGetDefaultResponse(BaseModel):
    """
    FooGetDefaultResponse
    """
    string: Optional[Foo] = None
    __properties = ["string"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FooGetDefaultResponse:
        """Create an instance of FooGetDefaultResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of string
        if self.string:
            _dict['string'] = self.string.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FooGetDefaultResponse:
        """Create an instance of FooGetDefaultResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FooGetDefaultResponse.parse_obj(obj)

        _obj = FooGetDefaultResponse.parse_obj({
            "string": Foo.from_dict(obj.get("string")) if obj.get("string") is not None else None
        })
        return _obj


