import requests
import json
from rich import print

target = "https://172.16.100.148/ins"
username = "admin"
password = "admin"

requestheader = {"content-type": "application/json"}
showcmd = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show vlan brief",
    "output_format": "json"
  }
}

# confcmd = {
#   "ins_api": {
#     "version": "1.0",
#     "type": "cli_conf",
#     "chunk": "0",
#     "sid": "1",
#     "input": "vlan 120 ;name TESTING_NETCONF_2 ;int Eth1/2 ;switchport access vlan 120",
#     "output_format": "json"
#   }
# }

response = requests.post(
    target,
    data=json.dumps(showcmd),
    # data=json.dumps(confcmd),
    headers= requestheader,
    auth=(username,password),
    verify=False,
).json()

print(response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['ip_addr'])

# print(json.dumps(response, indent=4, sort_keys=True))