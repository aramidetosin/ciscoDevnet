# https://github.com/datacenter/acitoolkit
from acitoolkit.acitoolkit import *
from pprint import pprint

url = "https://sandboxapicdc.cisco.com"
user = "admin"
pwd ="ciscopsdt"


session = Session(url,user, pwd)
session.login()

# tenants = Tenant.get(session)
# for tenant in tenants:
#     print(tenant.name)
#     print(tenant.descr)
#     print("*"*30)
#     print("")

# Create a new Tenant

new_tenant = Tenant("Tosin_Name_Here")
anp = AppProfile('Tosins_app', new_tenant)
epg = EPG("Tosins_epg", anp)

context = Context("Tosin_VRF", new_tenant)
bridge_domain = BridgeDomain("Tosin_bd", new_tenant)

bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

# Tenant is created here
print(new_tenant.get_url())
print(new_tenant.get_json())
# response = session.push_to_apic(new_tenant.get_url(), data=new_tenant.get_json())
# print(response)
#
# tenants = Tenant.get(session)
# for tenant in tenants:
#     if tenant.name == 'Tosin_Name_Here':
#         print(tenant.name)
#     else:
#         print(tenant.name)
#         print(tenant.descr)
#         print("*" * 30)
#         print("")

new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())