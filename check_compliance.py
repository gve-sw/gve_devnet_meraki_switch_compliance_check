#!/usr/bin/env python3
from env import *
from meraki import *
import pandas as pd


org_id = getOrgID(base_url, headers, org_name)
switches = getOrgSwitches(base_url, headers, org_id)

switch_ports = {}
switch_client_ports = []
for switch in switches:
    ports = getSwitchPorts(base_url, headers, switch["serial"])
    switch_ports[switch["serial"]] = ports

    clients = getClients(base_url, headers, switch["serial"])
    for client in clients:
        switch_client_ports.append(client["switchport"])

compliant_ports = []
noncompliant_ports = []

for switch in switch_ports:
    for port in switch_ports[switch]:
        port_id = port["portId"]
        enabled = port["enabled"]
        if port_id in switch_client_ports:
            connected = True
        else:
            connected = False

        if "accessPolicyType" in port.keys():
            access_policy_type = port["accessPolicyType"]
        else:
            access_policy_type = None

        if "stickyMacAllowList" in port.keys():
            sticky_mac_list = port["stickyMacAllowList"]
        else:
            sticky_mac_list = None

        if "stickyMacAllowListLimit" in port.keys():
            sticky_mac_limit = port["stickyMacAllowListLimit"]
        else:
            sticky_mac_limit = None

        port = {
            "Port": port_id,
            "Status": "Enabled" if enabled else "Disabled",
            "State": "Connected" if connected else "Disconnected",
            "Access Policy": access_policy_type,
            "Allow list size limit": sticky_mac_limit,
            "Allow listed MACs": sticky_mac_list,
            "Switch": switch
        }

        if enabled and access_policy_type == "Sticky MAC allow list" and sticky_mac_list and sticky_mac_limit:
            if sticky_mac_limit == len(sticky_mac_list):
                compliant_ports.append(port)
            else:
                noncompliant_ports.append(port)
        elif not enabled and access_policy_type == "Sticky MAC allow list" and sticky_mac_limit:
            if sticky_mac_limit == 1 and not sticky_mac_list:
                compliant_ports.append(port)
            else:
                noncompliant_ports.append(port)
        else:
            noncompliant_ports.append(port)

with pd.ExcelWriter('compliance_report.xlsx') as writer:
    compliant_df = pd.DataFrame.from_dict(compliant_ports)
    noncompliant_df = pd.DataFrame.from_dict(noncompliant_ports)

    compliant_df.to_excel(writer, sheet_name='Compliant ports')
    noncompliant_df.to_excel(writer, sheet_name='Noncompliant ports')
