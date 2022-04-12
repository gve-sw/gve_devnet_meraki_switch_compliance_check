# Meraki Switch Compliance Check
This prototype was built to create compliance reports for Meraki switch ports. The code accomplishes this by using Meraki APIs to pull switch port information from a given organization and then uses the logic diagrammed below to determine if the switch port meets compliance standards or not. Once it is determined which ports are compliant and which are not, an Excel report is generated that contains two worksheets, one for the compliant ports and one for the noncompliant ports.

![/IMAGES/switch_compliance_workflow.jpeg](/IMAGES/switch_compliance_workflow.jpeg)

## Contacts
* Danielle Stacy

## Solution Components
* Python 3.9
* Meraki APIs
* Meraki MS

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).


#### Organization Name
This code checks the compliance of all the switch ports within a Meraki organization. In order to accomplish this, you need to provide the name of the organization that you want to check the compliance of the switch ports from. To find the name of your organization, follow these instructions:
1. Login to the Meraki dashboard.
2. In the left-hand menu, select the Organization dropdown menu. It should be the first item in the menu.
3. All of the organizations should now be listed in the left-hand menu. To view a summary of the organizations, select the `MSP Portal` option. 
4. Note the name of the organization that you want to check the switch compliance of. You will need this name in the Installation portion of this prototype.

> For more information on MSP Portal, visit [this article](https://documentation.meraki.com/General_Administration/Inventory_and_Devices/Monitoring_and_Managing_Multiple_Organizations).


## Installation/Configuration
1. Clone this repository with `https://github.com/gve-sw/gve_devnet_meraki_switch_compliance_check`
2. Add Meraki API key and organization name to the env.py file
```python
API_KEY = "API key goes here"
org_name = "name of organization goes here"
```
3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
4. Install the requirements with `pip3 install -r requirements.txt`

## Usage
To run the program, use the command:
```
$ python3 check_compliance.py
```

Once the program is complete, a file will be created called compliance_report.xlsx. This report will detail the compliant and noncompliant switchports. The Excel workbook will have two different sheets, compliant and noncompliant. Both will give the details of the ports such as their status, state, access policy, allow list size limit, and allow listed MACs. For an enabled switchport to be compliant, the port should have an access policy of Sticky MAC allow list and its number of allowed listed MACs should be equal to the allow list size limit. For a disabled switchport to be compliant, it must also have an access policy of Sticky MAC allow list, but its number of allowed listed MACs should be 0 and its allow list size limit should be 1. The state has nothing to do with compliance and merely determines if a client is connected to that switchport or not.

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

The program creates a compliant ports sheet and noncompliant ports sheet in one Excel workbook.

Here is the compliant ports sheet:
![/IMAGES/compliant_ports_sheet.png](/IMAGES/compliant_ports_sheet.png)

Here is the noncompliants ports sheet:
![/IMAGES/noncompliant_ports_sheet.png](/IMAGES/noncompliant_ports_sheet.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
