import requests
from pprint import pprint as pp
import json

url = "https://172.16.100.138/api/aaaLogin.json"

payload = "{\n    \"aaaUser\":{\n        \"attributes\":{\n            \"name\": \"admin\",\n            \"pwd\": " \
          "\"admin\"\n        }\n    }\n} "
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Cookie': 'nxapi_auth=admin:bz6TJFGNpGzXN9VM5q5sd8L+gmY=; APIC-cookie=axrstowhCboY2jG7FvJKkUMe42yiVTUpmOfpKISNJeJBZeS0M+xpXkWAh577CCEMj3m+KnGpugfmpKqT1BO9MjhK3yeCNKxCZJvgEbSRbS/lTJfIGmomsLDD6OGK+TwrPGFs73Xko/AE0HCo/zJis2d0DQmhNHLGJvsmX7NY7BM='
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()

# pp(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']

cookies = {}
cookies['APIC-cookie'] = token

url = "https://172.16.100.138/api/node/mo/sys/intf/phys-[eth1/2].json"

payload = "{\n    \"l1PhysIf\":{\n        \"attributes\":{\n            \"descr\": \"TESTING WITH PYTHON\"\n        " \
          "}\n    }\n} "
headers = {
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
    'Content-Type': 'text/plain',
}

put_response = requests.put(url, headers=headers, data=payload, cookies=cookies, verify=False).json()

pp(put_response)
