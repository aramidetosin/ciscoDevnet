from dnacentersdk import DNACenterAPI
import json
import time
import calendar
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dna = DNACenterAPI(base_url='https://sandboxdnac.cisco.com:443',
                   username='devnetuser', password='Cisco123!', verify=False)

##### NETWORKS AND SITES ####

# # Print Site Topology
# sites = dna.sites.get_site()
# # pprint(sites)
#
# for site in sites['response']:
#     if site['parentId'] == '7b56c272-4ccd-4187-8820-b7b66fdce4be':
#         print(site['name'])
#         # print("*"*50)
#
#     for child_sites in sites['response']:
#         if child_sites['parentId'] == site['id']:
#             print(f"{child_sites['name']}")
#         for more_children in sites['response']:
#             if more_children['parentId'] == child_sites['id'] and child_sites['parentId'] == site['id']:
#                 print(f"           {more_children['name']}")
#     print(" ")
#
# vlans = dna.topology.get_vlan_details()
# for vlan in vlans['response']:
#     print(vlan)

# phys = dna.topology.get_physical_topology()
# print(json.dumps(phys, indent=2, sort_keys=True))


# devices = dna.devices.get_device_list()
# # print(json.dumps(devices,indent=2, sort_keys=True))
# for device in devices.response:
#     print(f"{device.type}")
#     print(f"         {device.hostname}")
#     print(f"         {device.managementIpAddress}")
#     print(f"         {device.id}")
#     print(" ")

# device = dna.devices.get_device_by_id("1cfd383a-7265-47fb-96b3-f069191a0ed5")
# pprint(device)

# epoch_datetime = calendar.timegm(time.gmtime())
# client_health = dna.clients.get_overall_client_health()
#
# print(json.dumps(client_health, indent=2, sort_keys=True))
# print(" ")

# net_health = dna.topology.get_overall_network_health()
# print(json.dumps(net_health, indent=2, sort_keys=True))

print(json.dumps(dna.sites.get_site_health(), indent=2, sort_keys=True))