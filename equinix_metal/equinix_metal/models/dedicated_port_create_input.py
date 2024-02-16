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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator

class DedicatedPortCreateInput(BaseModel):
    """
    DedicatedPortCreateInput
    """
    billing_account_name: Optional[StrictStr] = Field(None, description="The billing account name of the Equinix Fabric account.")
    contact_email: Optional[StrictStr] = Field(None, description="The preferred email used for communication and notifications about the Equinix Fabric interconnection. Required when using a Project API key. Optional and defaults to the primary user email address when using a User API key.")
    description: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    metro: StrictStr = Field(..., description="A Metro ID or code. For interconnections with Dedicated Ports, this will be the location of the issued Dedicated Ports.")
    mode: Optional[StrictStr] = Field(None, description="The mode of the interconnection (only relevant to Dedicated Ports). Fabric VCs won't have this field. Can be either 'standard' or 'tunnel'.   The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances.")
    name: StrictStr = Field(...)
    project: Optional[StrictStr] = None
    redundancy: StrictStr = Field(..., description="Either 'primary' or 'redundant'.")
    speed: Optional[StrictInt] = Field(None, description="A interconnection speed, in bps, mbps, or gbps. For Dedicated Ports, this can be 10Gbps or 100Gbps.")
    tags: Optional[conlist(StrictStr)] = None
    type: StrictStr = Field(..., description="When requesting for a dedicated port, the value of this field should be 'dedicated'.")
    use_case: Optional[StrictStr] = Field(None, description="The intended use case of the dedicated port.")
    __properties = ["billing_account_name", "contact_email", "description", "href", "metro", "mode", "name", "project", "redundancy", "speed", "tags", "type", "use_case"]

    @validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('standard', 'tunnel'):
            raise ValueError("must be one of enum values ('standard', 'tunnel')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('dedicated', 'shared', 'shared_port_vlan', 'shared_port_vlan_to_csp'):
            raise ValueError("must be one of enum values ('dedicated', 'shared', 'shared_port_vlan', 'shared_port_vlan_to_csp')")
        return value

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
    def from_json(cls, json_str: str) -> DedicatedPortCreateInput:
        """Create an instance of DedicatedPortCreateInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DedicatedPortCreateInput:
        """Create an instance of DedicatedPortCreateInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DedicatedPortCreateInput.parse_obj(obj)

        _obj = DedicatedPortCreateInput.parse_obj({
            "billing_account_name": obj.get("billing_account_name"),
            "contact_email": obj.get("contact_email"),
            "description": obj.get("description"),
            "href": obj.get("href"),
            "metro": obj.get("metro"),
            "mode": obj.get("mode"),
            "name": obj.get("name"),
            "project": obj.get("project"),
            "redundancy": obj.get("redundancy"),
            "speed": obj.get("speed"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "use_case": obj.get("use_case")
        })
        return _obj


