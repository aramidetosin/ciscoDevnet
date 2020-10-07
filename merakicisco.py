from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint as pp

token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()
pp(orgs)

# orgId = ""

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

# print(orgId)
# # pp(type(orgId))
#
params = {'organization_id': orgId}
network = meraki.networks.get_organization_networks(params)
# pp(network)

for network in network:
    if network['name'] == 'DevNet Sandbox ALWAYS ON':
        netId = network['id']

vlans = meraki.vlans.get_network_vlans(netId)
pp(vlans)
#
vlan = vlans[0]
vlan['name'] = "I was here"

updated_vlan = {}

updated_vlan['network_id'] = netId
updated_vlan['vlan_id'] = vlan['id']
updated_vlan['update_network_vlan'] = vlan

result = meraki.vlans.update_network_vlan(updated_vlan)
result_vlan = meraki.vlans.get_network_vlans(netId)


print(result_vlan)