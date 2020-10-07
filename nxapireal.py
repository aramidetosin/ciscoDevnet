import requests
import json
import re
from pprint import pprint as pp

switchuser = 'admin'
password = 'admin'

ip = '172.16.100.138'
url = f"https://{ip}/ins"

header = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp nei",
        "output_format": "json"
    }
}

response = requests.post(
    url,
    data=json.dumps(payload),
    headers=header,
    auth=(switchuser, password),
    verify=False,
).json()

##################### Login with NXAPI REST ###############################
auth_url = f"https://{ip}/api/mo/aaaLogin.json"

auth_body = {
    "aaaUser": {
        "attributes": {
            "name": switchuser,
            "pwd": password
        }
    }
}

auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()

# pp(response)
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

cookies = {}
cookies['APIC-cookie'] = token

counter = 0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']

while counter < nei_count:
    hostname = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
    local_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
    remote_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']

    body = {
        "l1PhysIf": {
            "attributes": {
                "descr": f"Connected to {hostname} Remote interface is {remote_int}"
            }
        }
    }

    counter += 1
    if local_int != 'mgmt0':
        int_name = str(local_int.lower()[:3])
        int_num = re.search(r'[1-9]/[1-9]*', local_int)
        int_url = f"https://{ip}/api/node/mo/sys/intf/phys-[{int_name}{str(int_num.group(0))}].json"
        post_response = requests.post(int_url, data=json.dumps(body), headers=header, cookies=cookies, verify=False).json()
        print(post_response)
