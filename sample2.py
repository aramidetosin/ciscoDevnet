from ncclient import manager
from pprint import pprint as pp
import xml.dom.minidom
m = manager.connect(host='172.16.100.132', port=830, username='cisco',
                    password='funtoa11', device_params={'name': 'csr'})

# for capability in m.server_capabilities:
#     print(capability)

netconf_reply = m.get_config("running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_filter = """
# <filter>
#   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#     <interface></interface>
#   </interfaces>
# </filter>"""
#
# netconf_reply = m.get_config("running", filter=netconf_filter)
#
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_interface_template = """
# <config>
#         <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#                 <interface>
#                         <name>Loopback1</name>
#                         <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
#                         <enabled>true</enabled>
#                         <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
#                                 <address>
#                                         <ip>1.1.1.1</ip>
#                                         <netmask>255.255.255.255</netmask>
#                                 </address>
#                         </ipv4>
#                 </interface>
#         </interfaces>
# </config>
# """
#
# netconf_reply = m.edit_config(netconf_interface_template, target = "running")
#
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_interface_template = """
# <config>
#         <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#                 <interface operation="delete">
#                         <name>Loopback1</name>
#                 </interface>
#         </interfaces>
# </config>
# """
#
# netconf_reply = m.edit_config(netconf_interface_template, target = "running")
#
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


m.close_session()