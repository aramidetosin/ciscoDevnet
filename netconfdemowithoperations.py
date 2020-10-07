import requests
import json
from ncclient import manager
import xmltodict
import xml.dom.minidom
from pprint import pprint as pp
from rich import print

ios_xe_host = "172.16.100.146"
ios_xe_port = 830
ios_xe_username = "cisco"
ios_xe_password = "cisco"

with manager.connect(
        host=ios_xe_host,
        port=ios_xe_port,
        username=ios_xe_username,
        password=ios_xe_password,
        hostkey_verify=False,
        look_for_keys=False
) as m:
    # netconf_filter = """
    # <filter>
    #   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    #     <interface>
    #       <name>GigabitEthernet1</name>
    #     </interface>
    #   </interfaces>
    #   <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    #     <interface>
    #       <name>GigabitEthernet1</name>
    #     </interface>
    #   </interfaces-state>
    # </filter>"""


#
# /ietf-routing:routing-state/ribs/rib/routes/route/next-hop/outgoing-interface

    netconf_filter = """
<filter>
<routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
    <routing-instance>
        <name>default</name>
        <type>default-routing-instance</type>
        <router-id>0.0.0.0</router-id>
        <ribs>
            <rib>
                <name>ipv4-default</name>
                <address-family>ipv4</address-family>
                <default-rib>false</default-rib>
                <routes>
                    <route>
                        <destination-prefix>1.1.1.1</destination-prefix>
                        <route-preference>110</route-preference>
                        <metric>110</metric>
                        <next-hop>
                            <outgoing-interface>GigabitEthernet2</outgoing-interface>
                            <next-hop-address>10.1.1.2</next-hop-address>
                        </next-hop>
                        <source-protocol xmlns:ospf="urn:ietf:params:xml:ns:yang:ietf-ospf">ospf:ospfv2</source-protocol>
                        <active/>
                    </route>
                </routes>
            </rib>
        </ribs>
    </routing-instance>
</routing-state>
</filter>"""

    interface_netconf = m.get(netconf_filter)
    print('getting running config')
    xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    # print(xmlDom.toprettyxml(indent="  "))
    print('*' * 25 + "Break " + "*" * 50)
    interface_python = xmltodict.parse(interface_netconf.xml)['rpc-reply']['data']
    route = interface_python['routing-state']['routing-instance']['ribs']['rib']['routes']['route']['destination-prefix']['#text']
    outgoing_iface = interface_python['routing-state']['routing-instance']['ribs']['rib']['routes']['route']['next-hop']['outgoing-interface']

    print(f"{route} has outgoing interface of [yellow]{outgoing_iface}[/yellow]")
#
#     config = interface_python['interfaces']['interface']
#     op_state = interface_python['interfaces-state']['interface']
#     print(f"[green]START[/green]")
#
#     print(f"[red]NAME: {config['name']['#text']}[/red]")
#     print(f"Description: {config['description']}".upper())
#     print(f"{op_state['statistics']['in-unicast-pkts']}")
#     print(f"{op_state['phys-address']}")