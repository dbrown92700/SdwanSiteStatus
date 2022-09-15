#!/usr/bin/python3
"""
Copyright (c) 2012 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
__author__ = "David Brown <davibrow@cisco.com>"
__contributors__ = []
__copyright__ = "Copyright (c) 2012 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
from vmanage_api import rest_api_lib
from includes import *

system_ips = ['10.46.16.186','10.46.18.58','10.46.18.5','10.46.16.122']

if __name__ == '__main__':

    vmanage = rest_api_lib(vmanage_address, vmanage_user, vmanage_password)
    for ip in system_ips:
        url = f'/device/control/summary?deviceId={ip}'
        control_connections = vmanage.get_request(url)
        try:
            print(f'{ip}: vManage:{control_connections["data"][0]["vmanage_counts"]} vSmart:{control_connections["data"][0]["vsmart_counts"]}')
        except Exception as e:
            print(f'{ip}: Not Found')
# [END gae_python38_app]


