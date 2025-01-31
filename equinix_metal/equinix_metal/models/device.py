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
from equinix_metal.models.device_actions_inner import DeviceActionsInner
from equinix_metal.models.device_created_by import DeviceCreatedBy
from equinix_metal.models.device_metro import DeviceMetro
from equinix_metal.models.device_project_lite import DeviceProjectLite
from equinix_metal.models.event import Event
from equinix_metal.models.facility import Facility
from equinix_metal.models.href import Href
from equinix_metal.models.ip_assignment import IPAssignment
from equinix_metal.models.operating_system import OperatingSystem
from equinix_metal.models.plan import Plan
from equinix_metal.models.port import Port
from equinix_metal.models.project import Project
from equinix_metal.models.storage import Storage

class Device(BaseModel):
    """
    Device
    """
    actions: Optional[conlist(DeviceActionsInner)] = Field(None, description="Actions supported by the device instance.")
    always_pxe: Optional[StrictBool] = None
    billing_cycle: Optional[StrictStr] = None
    bonding_mode: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    created_by: Optional[DeviceCreatedBy] = None
    customdata: Optional[Dict[str, Any]] = None
    description: Optional[StrictStr] = None
    facility: Optional[Facility] = None
    firmware_set_id: Optional[StrictStr] = Field(None, description="The UUID of the firmware set to associate with the device.")
    hardware_reservation: Optional[HardwareReservation] = None
    hostname: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    ip_addresses: Optional[conlist(IPAssignment)] = None
    ipxe_script_url: Optional[StrictStr] = None
    iqn: Optional[StrictStr] = None
    locked: Optional[StrictBool] = Field(None, description="Prevents accidental deletion of this resource when set to true.")
    metro: Optional[DeviceMetro] = None
    network_frozen: Optional[StrictBool] = Field(None, description="Whether network mode changes such as converting to/from Layer2 or Layer3 networking, bonding or disbonding network interfaces are permitted for the device.")
    network_ports: Optional[conlist(Port)] = Field(None, description="By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.")
    operating_system: Optional[OperatingSystem] = None
    plan: Optional[Plan] = None
    project: Optional[Project] = None
    project_lite: Optional[DeviceProjectLite] = None
    provisioning_events: Optional[conlist(Event)] = None
    provisioning_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Only visible while device provisioning")
    root_password: Optional[StrictStr] = Field(None, description="Root password is automatically generated when server is provisioned and it is removed after 24 hours")
    short_id: Optional[StrictStr] = None
    sos: Optional[StrictStr] = Field(None, description="Hostname used to connect to the instance via the SOS (Serial over SSH) out-of-band console.")
    spot_instance: Optional[StrictBool] = Field(None, description="Whether or not the device is a spot instance.")
    spot_price_max: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown.")
    ssh_keys: Optional[conlist(Href)] = None
    state: Optional[StrictStr] = Field(None, description="The current state the instance is in.  * When an instance is initially created it will be in the `queued` state until it is picked up by the provisioner. * Once provisioning has begun on the instance it's state will move to `provisioning`. * When an instance is deleted, it will move to `deprovisioning` state until the deprovision is completed and the instance state moves to `deleted`. * If an instance fails to provision or deprovision it will move to `failed` state. * Once an instance has completed provisioning it will move to `active` state. * If an instance is currently powering off or powering on it will move to `powering_off` or `powering_on` states respectively.  * When the instance is powered off completely it will move to the `inactive` state. * When an instance is powered on completely it will move to the `active` state. * Using the reinstall action to install a new OS on the instance will cause the instance state to change to `reinstalling`. * When the reinstall action is complete the instance will move to `active` state.")
    storage: Optional[Storage] = None
    switch_uuid: Optional[StrictStr] = Field(None, description="Switch short id. This can be used to determine if two devices are connected to the same switch, for example.")
    tags: Optional[conlist(StrictStr)] = None
    termination_time: Optional[datetime] = Field(None, description="When the device will be terminated. If you don't supply timezone info, the timestamp is assumed to be in UTC.  This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.")
    updated_at: Optional[datetime] = None
    user: Optional[StrictStr] = None
    userdata: Optional[StrictStr] = None
    volumes: Optional[conlist(Href)] = None
    __properties = ["actions", "always_pxe", "billing_cycle", "bonding_mode", "created_at", "created_by", "customdata", "description", "facility", "firmware_set_id", "hardware_reservation", "hostname", "href", "id", "image_url", "ip_addresses", "ipxe_script_url", "iqn", "locked", "metro", "network_frozen", "network_ports", "operating_system", "plan", "project", "project_lite", "provisioning_events", "provisioning_percentage", "root_password", "short_id", "sos", "spot_instance", "spot_price_max", "ssh_keys", "state", "storage", "switch_uuid", "tags", "termination_time", "updated_at", "user", "userdata", "volumes"]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('queued', 'provisioning', 'deprovisioning', 'reinstalling', 'active', 'inactive', 'failed', 'powering_on', 'powering_off', 'deleted'):
            raise ValueError("must be one of enum values ('queued', 'provisioning', 'deprovisioning', 'reinstalling', 'active', 'inactive', 'failed', 'powering_on', 'powering_off', 'deleted')")
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
    def from_json(cls, json_str: str) -> Device:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hardware_reservation
        if self.hardware_reservation:
            _dict['hardware_reservation'] = self.hardware_reservation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ip_addresses (list)
        _items = []
        if self.ip_addresses:
            for _item in self.ip_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ip_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in network_ports (list)
        _items = []
        if self.network_ports:
            for _item in self.network_ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['network_ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of operating_system
        if self.operating_system:
            _dict['operating_system'] = self.operating_system.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_lite
        if self.project_lite:
            _dict['project_lite'] = self.project_lite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in provisioning_events (list)
        _items = []
        if self.provisioning_events:
            for _item in self.provisioning_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['provisioning_events'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Device:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Device.parse_obj(obj)

        _obj = Device.parse_obj({
            "actions": [DeviceActionsInner.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "always_pxe": obj.get("always_pxe"),
            "billing_cycle": obj.get("billing_cycle"),
            "bonding_mode": obj.get("bonding_mode"),
            "created_at": obj.get("created_at"),
            "created_by": DeviceCreatedBy.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "customdata": obj.get("customdata"),
            "description": obj.get("description"),
            "facility": Facility.from_dict(obj.get("facility")) if obj.get("facility") is not None else None,
            "firmware_set_id": obj.get("firmware_set_id"),
            "hardware_reservation": HardwareReservation.from_dict(obj.get("hardware_reservation")) if obj.get("hardware_reservation") is not None else None,
            "hostname": obj.get("hostname"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "image_url": obj.get("image_url"),
            "ip_addresses": [IPAssignment.from_dict(_item) for _item in obj.get("ip_addresses")] if obj.get("ip_addresses") is not None else None,
            "ipxe_script_url": obj.get("ipxe_script_url"),
            "iqn": obj.get("iqn"),
            "locked": obj.get("locked"),
            "metro": DeviceMetro.from_dict(obj.get("metro")) if obj.get("metro") is not None else None,
            "network_frozen": obj.get("network_frozen"),
            "network_ports": [Port.from_dict(_item) for _item in obj.get("network_ports")] if obj.get("network_ports") is not None else None,
            "operating_system": OperatingSystem.from_dict(obj.get("operating_system")) if obj.get("operating_system") is not None else None,
            "plan": Plan.from_dict(obj.get("plan")) if obj.get("plan") is not None else None,
            "project": Project.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "project_lite": DeviceProjectLite.from_dict(obj.get("project_lite")) if obj.get("project_lite") is not None else None,
            "provisioning_events": [Event.from_dict(_item) for _item in obj.get("provisioning_events")] if obj.get("provisioning_events") is not None else None,
            "provisioning_percentage": obj.get("provisioning_percentage"),
            "root_password": obj.get("root_password"),
            "short_id": obj.get("short_id"),
            "sos": obj.get("sos"),
            "spot_instance": obj.get("spot_instance"),
            "spot_price_max": obj.get("spot_price_max"),
            "ssh_keys": [Href.from_dict(_item) for _item in obj.get("ssh_keys")] if obj.get("ssh_keys") is not None else None,
            "state": obj.get("state"),
            "storage": Storage.from_dict(obj.get("storage")) if obj.get("storage") is not None else None,
            "switch_uuid": obj.get("switch_uuid"),
            "tags": obj.get("tags"),
            "termination_time": obj.get("termination_time"),
            "updated_at": obj.get("updated_at"),
            "user": obj.get("user"),
            "userdata": obj.get("userdata"),
            "volumes": [Href.from_dict(_item) for _item in obj.get("volumes")] if obj.get("volumes") is not None else None
        })
        return _obj

from equinix_metal.models.hardware_reservation import HardwareReservation
Device.update_forward_refs()

