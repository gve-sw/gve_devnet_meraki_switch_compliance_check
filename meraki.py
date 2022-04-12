#!/usr/bin/env python3
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
