#!/usr/bin/env python3
base_url = "https://api.meraki.com/api/v1"
api_key = "API KEY goes here"
org_name = "name of organization goes here"

headers = {
    "X-Cisco-Meraki-API-Key": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json"
}
