# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from equinix_metal.models.facility import Facility
from equinix_metal.models.plan import Plan
from equinix_metal.models.project import Project

class HardwareReservation(BaseModel):
    """
    HardwareReservation
    """
    created_at: Optional[datetime] = None
    custom_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Amount that will be charged for every billing_cycle.")
    device: Optional[Device] = None
    facility: Optional[Facility] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    need_of_service: Optional[StrictBool] = Field(None, description="Whether this Device requires assistance from Equinix Metal.")
    plan: Optional[Plan] = None
    project: Optional[Project] = None
    provisionable: Optional[StrictBool] = Field(None, description="Whether the reserved server is provisionable or not. Spare devices can't be provisioned unless they are activated first.")
    short_id: Optional[StrictStr] = Field(None, description="Short version of the ID.")
    spare: Optional[StrictBool] = Field(None, description="Whether the Hardware Reservation is a spare. Spare Hardware Reservations are used when a Hardware Reservations requires service from Equinix Metal")
    switch_uuid: Optional[StrictStr] = Field(None, description="Switch short id. This can be used to determine if two devices are connected to the same switch, for example.")
    termination_time: Optional[datetime] = Field(None, description="Expiration date for the reservation.")
    __properties = ["created_at", "custom_rate", "device", "facility", "href", "id", "need_of_service", "plan", "project", "provisionable", "short_id", "spare", "switch_uuid", "termination_time"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HardwareReservation:
        """Create an instance of HardwareReservation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HardwareReservation:
        """Create an instance of HardwareReservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HardwareReservation.parse_obj(obj)

        _obj = HardwareReservation.parse_obj({
            "created_at": obj.get("created_at"),
            "custom_rate": obj.get("custom_rate"),
            "device": Device.from_dict(obj.get("device")) if obj.get("device") is not None else None,
            "facility": Facility.from_dict(obj.get("facility")) if obj.get("facility") is not None else None,
            "href": obj.get("href"),
            "id": obj.get("id"),
            "need_of_service": obj.get("need_of_service"),
            "plan": Plan.from_dict(obj.get("plan")) if obj.get("plan") is not None else None,
            "project": Project.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "provisionable": obj.get("provisionable"),
            "short_id": obj.get("short_id"),
            "spare": obj.get("spare"),
            "switch_uuid": obj.get("switch_uuid"),
            "termination_time": obj.get("termination_time")
        })
        return _obj

from equinix_metal.models.device import Device
HardwareReservation.update_forward_refs()

