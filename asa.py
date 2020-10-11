import requests
import json

url = "https://172.16.100.170/api/routing/static"
# h = "172.16.100.170"

# url = f"https://{h}/api/interfaces/physical"

# url = f"https://{h}/api/monitoring/connections"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

userpw = ('cisco', 'cisco')

get_response = requests.get(
    url, headers=headers, auth=userpw, verify=False).json()['items']

print(json.dumps(get_response, indent=2, sort_keys=True))

# for item in get_response:
#     print(item['sourceIp'])
#     print(item['destinationIp'])