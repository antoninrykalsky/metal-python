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
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from equinix_metal.models.ip_address import IPAddress
from equinix_metal.models.ssh_key_input import SSHKeyInput
from equinix_metal.models.storage import Storage

class DeviceCreateInMetroInput(BaseModel):
    """
    DeviceCreateInMetroInput
    """
    href: Optional[StrictStr] = None
    metro: StrictStr = Field(..., description="Metro code or ID of where the instance should be provisioned in. Either metro or facility must be provided.")
    always_pxe: Optional[StrictBool] = Field(None, description="When true, devices with a `custom_ipxe` OS will always boot to iPXE. The default setting of false ensures that iPXE will be used on only the first boot.")
    billing_cycle: Optional[StrictStr] = Field(None, description="The billing cycle of the device.")
    customdata: Optional[Dict[str, Any]] = Field(None, description="Customdata is an arbitrary JSON value that can be accessed via the metadata service.")
    description: Optional[StrictStr] = Field(None, description="Any description of the device or how it will be used. This may be used to inform other API consumers with project access.")
    features: Optional[conlist(StrictStr)] = Field(None, description="The features attribute allows you to optionally specify what features your server should have.  In the API shorthand syntax, all features listed are `required`:  ``` { \"features\": [\"tpm\"] } ```  Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a `preferred` value. The request will not fail if we have no servers with that feature in our inventory. The API offers an alternative syntax for mixing preferred and required features:  ``` { \"features\": { \"tpm\": \"required\", \"raid\": \"preferred\" } } ```  The request will only fail if there are no available servers matching the required `tpm` criteria.")
    hardware_reservation_id: Optional[StrictStr] = Field(None, description="The Hardware Reservation UUID to provision. Alternatively, `next-available` can be specified to select from any of the available hardware reservations. An error will be returned if the requested reservation option is not available.  See [Reserved Hardware](https://metal.equinix.com/developers/docs/deploy/reserved/) for more details.")
    hostname: Optional[StrictStr] = Field(None, description="The hostname to use within the operating system. The same hostname may be used on multiple devices within a project.")
    ip_addresses: Optional[conlist(IPAddress)] = Field(None, description="The `ip_addresses attribute will allow you to specify the addresses you want created with your device.  The default value configures public IPv4, public IPv6, and private IPv4.  Private IPv4 address is required. When specifying `ip_addresses`, one of the array items must enable private IPv4.  Some operating systems require public IPv4 address. In those cases you will receive an error message if public IPv4 is not enabled.  For example, to only configure your server with a private IPv4 address, you can send `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": false }] }`.  It is possible to request a subnet size larger than a `/30` by assigning addresses using the UUID(s) of ip_reservations in your project.  For example, `{ \"ip_addresses\": [..., {\"address_family\": 4, \"public\": true, \"ip_reservations\": [\"uuid1\", \"uuid2\"]}] }`  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or proxy through another server in the project with public IPs enabled.")
    ipxe_script_url: Optional[StrictStr] = Field(None, description="When set, the device will chainload an iPXE Script at boot fetched from the supplied URL.  See [Custom iPXE](https://metal.equinix.com/developers/docs/operating-systems/custom-ipxe/) for more details.")
    locked: Optional[StrictBool] = Field(False, description="Whether the device should be locked, preventing accidental deletion.")
    network_frozen: Optional[StrictBool] = Field(None, description="If true, this instance can not be converted to a different network type.")
    no_ssh_keys: Optional[StrictBool] = Field(False, description="Overrides default behaviour of attaching all of the organization members ssh keys and project ssh keys to device if no specific keys specified")
    operating_system: StrictStr = Field(..., description="The slug of the operating system to provision. Check the Equinix Metal operating system documentation for rules that may be imposed per operating system, including restrictions on IP address options and device plans.")
    plan: StrictStr = Field(..., description="The slug of the device plan to provision.")
    private_ipv4_subnet_size: Optional[StrictInt] = Field(28, description="Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device.")
    project_ssh_keys: Optional[conlist(StrictStr)] = Field(None, description="A list of UUIDs identifying the device parent project that should be authorized to access this device (typically via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.  If no SSH keys are specified (`user_ssh_keys`, `project_ssh_keys`, and `ssh_keys` are all empty lists or omitted), all parent project keys, parent project members keys and organization members keys will be included. This behaviour can be changed with 'no_ssh_keys' option to omit any SSH key being added. ")
    public_ipv4_subnet_size: Optional[StrictInt] = Field(31, description="Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request.")
    spot_instance: Optional[StrictBool] = Field(None, description="Create a spot instance. Spot instances are created with a maximum bid price. If the bid price is not met, the spot instance will be terminated as indicated by the `termination_time` field.")
    spot_price_max: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The maximum amount to bid for a spot instance.")
    ssh_keys: Optional[conlist(SSHKeyInput)] = Field(None, description="A list of new or existing project ssh_keys that should be authorized to access this device (typically via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.  These keys are added in addition to any keys defined by   `project_ssh_keys` and `user_ssh_keys`. ")
    storage: Optional[Storage] = None
    tags: Optional[conlist(StrictStr)] = None
    termination_time: Optional[datetime] = Field(None, description="When the device will be terminated. If you don't supply timezone info, the timestamp is assumed to be in UTC.  This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid. ")
    user_ssh_keys: Optional[conlist(StrictStr)] = Field(None, description="A list of UUIDs identifying the users that should be authorized to access this device (typically via /root/.ssh/authorized_keys).  These keys will also appear in the device metadata.  The users must be members of the project or organization.  If no SSH keys are specified (`user_ssh_keys`, `project_ssh_keys`, and `ssh_keys` are all empty lists or omitted), all parent project keys, parent project members keys and organization members keys will be included. This behaviour can be changed with 'no_ssh_keys' option to omit any SSH key being added. ")
    userdata: Optional[StrictStr] = Field(None, description="The userdata presented in the metadata service for this device.  Userdata is fetched and interpreted by the operating system installed on the device. Acceptable formats are determined by the operating system, with the exception of a special iPXE enabling syntax which is handled before the operating system starts.  See [Server User Data](https://metal.equinix.com/developers/docs/servers/user-data/) and [Provisioning with Custom iPXE](https://metal.equinix.com/developers/docs/operating-systems/custom-ipxe/#provisioning-with-custom-ipxe) for more details.")
    __properties = ["href", "metro", "always_pxe", "billing_cycle", "customdata", "description", "features", "hardware_reservation_id", "hostname", "ip_addresses", "ipxe_script_url", "locked", "network_frozen", "no_ssh_keys", "operating_system", "plan", "private_ipv4_subnet_size", "project_ssh_keys", "public_ipv4_subnet_size", "spot_instance", "spot_price_max", "ssh_keys", "storage", "tags", "termination_time", "user_ssh_keys", "userdata"]

    @validator('billing_cycle')
    def billing_cycle_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('hourly', 'daily', 'monthly', 'yearly'):
            raise ValueError("must be one of enum values ('hourly', 'daily', 'monthly', 'yearly')")
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
    def from_json(cls, json_str: str) -> DeviceCreateInMetroInput:
        """Create an instance of DeviceCreateInMetroInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ip_addresses (list)
        _items = []
        if self.ip_addresses:
            for _item in self.ip_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ip_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssh_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict['storage'] = self.storage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceCreateInMetroInput:
        """Create an instance of DeviceCreateInMetroInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeviceCreateInMetroInput.parse_obj(obj)

        _obj = DeviceCreateInMetroInput.parse_obj({
            "href": obj.get("href"),
            "metro": obj.get("metro"),
            "always_pxe": obj.get("always_pxe"),
            "billing_cycle": obj.get("billing_cycle"),
            "customdata": obj.get("customdata"),
            "description": obj.get("description"),
            "features": obj.get("features"),
            "hardware_reservation_id": obj.get("hardware_reservation_id"),
            "hostname": obj.get("hostname"),
            "ip_addresses": [IPAddress.from_dict(_item) for _item in obj.get("ip_addresses")] if obj.get("ip_addresses") is not None else None,
            "ipxe_script_url": obj.get("ipxe_script_url"),
            "locked": obj.get("locked") if obj.get("locked") is not None else False,
            "network_frozen": obj.get("network_frozen"),
            "no_ssh_keys": obj.get("no_ssh_keys") if obj.get("no_ssh_keys") is not None else False,
            "operating_system": obj.get("operating_system"),
            "plan": obj.get("plan"),
            "private_ipv4_subnet_size": obj.get("private_ipv4_subnet_size") if obj.get("private_ipv4_subnet_size") is not None else 28,
            "project_ssh_keys": obj.get("project_ssh_keys"),
            "public_ipv4_subnet_size": obj.get("public_ipv4_subnet_size") if obj.get("public_ipv4_subnet_size") is not None else 31,
            "spot_instance": obj.get("spot_instance"),
            "spot_price_max": obj.get("spot_price_max"),
            "ssh_keys": [SSHKeyInput.from_dict(_item) for _item in obj.get("ssh_keys")] if obj.get("ssh_keys") is not None else None,
            "storage": Storage.from_dict(obj.get("storage")) if obj.get("storage") is not None else None,
            "tags": obj.get("tags"),
            "termination_time": obj.get("termination_time"),
            "user_ssh_keys": obj.get("user_ssh_keys"),
            "userdata": obj.get("userdata")
        })
        return _obj


