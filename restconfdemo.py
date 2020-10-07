import requests
import json
from pprint import pprint as pp
from rich import box, print, table, console
import itertools

m = {
    'ip': '172.16.100.146',
    'port': 443,
    'user': 'cisco',
    'password': 'cisco',
    'hostkey_verify': False,
    'look_for_keys': False
}

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

interfaces = 'GigabitEthernet1'

url = f"https://{m['ip']}:{m['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface={interfaces}"

response = requests.get(url, headers=headers, auth=(m['user'], m['password']), verify=False)

api_data = response.json()

print("*"*50)
print(f"[red]{api_data['Cisco-IOS-XE-interfaces-oper:interface']['description']}[/red]")
print("*"*50)
if api_data['Cisco-IOS-XE-interfaces-oper:interface']['admin-status'] == 'if-state-up':
    print(f"Interface [yellow]{interfaces}[/yellow] is UP with inUtilization of {api_data['Cisco-IOS-XE-interfaces-oper:interface']['statistics']['in-unicast-pkts']}")
