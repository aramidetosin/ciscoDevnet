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
    # m = manager.connect(
    #     host=ios_xe_host,
    #     port=ios_xe_port,
    #     username=ios_xe_username,
    #     password=ios_xe_password,
    #     hostkey_verify=False,
    #     look_for_keys=False
    # )

    netconf_filter = """
    <filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet1</name>
        </interface>
      </interfaces>
    </filter>"""

    for capability in m.server_capabilities:
        print("*" * 50)
        print(capability)
    print('Connected')
    interface_netconf = m.get_config('running', netconf_filter)
    print('getting running config')
    xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    print(xmlDom.toprettyxml(indent="  "))
    print('*' * 25 + "Break " + "*" * 50)
    interface_python = xmltodict.parse(interface_netconf.xml)['rpc-reply']['data']
    name = interface_python['interfaces']['interface']['name']['#text']
    intf_ip = interface_python['interfaces']['interface']['ipv4']['address']['ip']
    subnet = interface_python['interfaces']['interface']['ipv4']['address']['netmask']
    print(f"[yellow]{name}[/yellow] ====> {intf_ip} {subnet}")
# m.close_session()