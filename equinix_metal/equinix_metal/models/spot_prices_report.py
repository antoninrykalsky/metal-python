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


from typing import Optional
from pydantic import BaseModel, StrictStr
from equinix_metal.models.spot_prices_per_facility import SpotPricesPerFacility
from equinix_metal.models.spot_prices_per_new_facility import SpotPricesPerNewFacility

class SpotPricesReport(BaseModel):
    """
    SpotPricesReport
    """
    ams1: Optional[SpotPricesPerFacility] = None
    atl1: Optional[SpotPricesPerNewFacility] = None
    dfw1: Optional[SpotPricesPerNewFacility] = None
    ewr1: Optional[SpotPricesPerFacility] = None
    fra1: Optional[SpotPricesPerNewFacility] = None
    href: Optional[StrictStr] = None
    iad1: Optional[SpotPricesPerNewFacility] = None
    lax1: Optional[SpotPricesPerNewFacility] = None
    nrt1: Optional[SpotPricesPerFacility] = None
    ord1: Optional[SpotPricesPerNewFacility] = None
    sea1: Optional[SpotPricesPerNewFacility] = None
    sin1: Optional[SpotPricesPerNewFacility] = None
    sjc1: Optional[SpotPricesPerFacility] = None
    syd1: Optional[SpotPricesPerNewFacility] = None
    yyz1: Optional[SpotPricesPerNewFacility] = None
    __properties = ["ams1", "atl1", "dfw1", "ewr1", "fra1", "href", "iad1", "lax1", "nrt1", "ord1", "sea1", "sin1", "sjc1", "syd1", "yyz1"]

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
    def from_json(cls, json_str: str) -> SpotPricesReport:
        """Create an instance of SpotPricesReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ams1
        if self.ams1:
            _dict['ams1'] = self.ams1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of atl1
        if self.atl1:
            _dict['atl1'] = self.atl1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dfw1
        if self.dfw1:
            _dict['dfw1'] = self.dfw1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ewr1
        if self.ewr1:
            _dict['ewr1'] = self.ewr1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fra1
        if self.fra1:
            _dict['fra1'] = self.fra1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iad1
        if self.iad1:
            _dict['iad1'] = self.iad1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lax1
        if self.lax1:
            _dict['lax1'] = self.lax1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nrt1
        if self.nrt1:
            _dict['nrt1'] = self.nrt1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ord1
        if self.ord1:
            _dict['ord1'] = self.ord1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sea1
        if self.sea1:
            _dict['sea1'] = self.sea1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sin1
        if self.sin1:
            _dict['sin1'] = self.sin1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sjc1
        if self.sjc1:
            _dict['sjc1'] = self.sjc1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of syd1
        if self.syd1:
            _dict['syd1'] = self.syd1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of yyz1
        if self.yyz1:
            _dict['yyz1'] = self.yyz1.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpotPricesReport:
        """Create an instance of SpotPricesReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpotPricesReport.parse_obj(obj)

        _obj = SpotPricesReport.parse_obj({
            "ams1": SpotPricesPerFacility.from_dict(obj.get("ams1")) if obj.get("ams1") is not None else None,
            "atl1": SpotPricesPerNewFacility.from_dict(obj.get("atl1")) if obj.get("atl1") is not None else None,
            "dfw1": SpotPricesPerNewFacility.from_dict(obj.get("dfw1")) if obj.get("dfw1") is not None else None,
            "ewr1": SpotPricesPerFacility.from_dict(obj.get("ewr1")) if obj.get("ewr1") is not None else None,
            "fra1": SpotPricesPerNewFacility.from_dict(obj.get("fra1")) if obj.get("fra1") is not None else None,
            "href": obj.get("href"),
            "iad1": SpotPricesPerNewFacility.from_dict(obj.get("iad1")) if obj.get("iad1") is not None else None,
            "lax1": SpotPricesPerNewFacility.from_dict(obj.get("lax1")) if obj.get("lax1") is not None else None,
            "nrt1": SpotPricesPerFacility.from_dict(obj.get("nrt1")) if obj.get("nrt1") is not None else None,
            "ord1": SpotPricesPerNewFacility.from_dict(obj.get("ord1")) if obj.get("ord1") is not None else None,
            "sea1": SpotPricesPerNewFacility.from_dict(obj.get("sea1")) if obj.get("sea1") is not None else None,
            "sin1": SpotPricesPerNewFacility.from_dict(obj.get("sin1")) if obj.get("sin1") is not None else None,
            "sjc1": SpotPricesPerFacility.from_dict(obj.get("sjc1")) if obj.get("sjc1") is not None else None,
            "syd1": SpotPricesPerNewFacility.from_dict(obj.get("syd1")) if obj.get("syd1") is not None else None,
            "yyz1": SpotPricesPerNewFacility.from_dict(obj.get("yyz1")) if obj.get("yyz1") is not None else None
        })
        return _obj


