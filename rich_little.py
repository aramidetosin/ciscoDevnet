import littletable as lt
from rich import box, print

people = lt.Table().csv_import("""\
Name,Age,Sex
Tosin,34,Male
Dami,32,Female""")

print(f'[green]PASSED[/green]')
people.present(box=box.SQUARE)


import requests
import json
from pprint import pprint as pp


m ={
    "ip": 'ios-xe-mgmt.cisco.com',
    'port': '9443',
    'user': 'developer',
    'password': 'C1sco12345'
}

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json'
}

# url = f"https://{m['ip']}:{m['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=lo0"
url = f"https://{m['ip']}:{m['port']}/restconf/data/ietf-interfaces:interfaces"

# print(url)
response = requests.get(url, headers=headers, auth=(m['user'], m['password']),verify=False)

# print(response.json())
api_data = response.json()
print(api_data['ietf-interfaces:interfaces']['interface'])
for i in api_data['ietf-interfaces:interfaces']['interface']:
    print(f"{i['name']}========>{i['description']}")
# pp(api_data['Cisco-IOS-XE-interfaces-oper:interface']['description'])
# if api_data['Cisco-IOS-XE-interfaces-oper:interface']['admin-status'] == 'if-state-up':
#     print('Interface is up')