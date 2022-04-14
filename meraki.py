#!/usr/bin/env python3
'''
Copyright (c) 2020 Cisco and/or its affiliates.
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
'''
import requests
import json


def getOrgID(base_url, headers, org_name):
    organizations_endpoint = "/organizations"
    orgs = json.loads(requests.get(base_url+organizations_endpoint, headers=headers).text)

    for org in orgs:
        if org["name"] == org_name:
            org_id = org["id"]

            return org_id

    return None


def getOrgSwitches(base_url, headers, org_id):
    devices_endpoint = "/organizations/{}/devices".format(org_id)
    devices = json.loads(requests.get(base_url+devices_endpoint, headers=headers).text)

    switches = []
    for device in devices:
        if device["productType"] == "switch":
            switches.append(device)

    return switches


def getSwitchPorts(base_url, headers, serial):
    switch_ports_endpoint = "/devices/{}/switch/ports".format(serial)
    ports = json.loads(requests.get(base_url+switch_ports_endpoint, headers=headers).text)

    return ports


def getClients(base_url, headers, serial):
    clients_endpoint = "/devices/{}/clients".format(serial)
    clients = json.loads(requests.get(base_url+clients_endpoint, headers=headers).text)

    return clients
