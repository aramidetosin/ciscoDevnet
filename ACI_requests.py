import requests
import json
from pprint import pprint as pp

# Get token
url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"
payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}

headers = {
    'Content-Type': 'application/json'
}


response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
# print(json.dumps(response, indent=2, sort_keys=True))

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token

# Get Application profile


application_profile_url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"
headers = {
    "cache-control": "no-cache"
}

get_response = requests.get(application_profile_url, headers=headers, cookies=cookies, verify=False).json()
print(json.dumps(get_response, indent=2, sort_keys=True))

# Update APN DESCRIPTION


payload = {
    "fvAp": {
        "attributes": {
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}

post_response = requests.post(application_profile_url, headers=headers, cookies=cookies, verify=False, data=json.dumps(payload)).json()
get_response = requests.get(application_profile_url, headers=headers, cookies=cookies, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))