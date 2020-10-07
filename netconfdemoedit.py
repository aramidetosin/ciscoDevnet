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

iface_name = "GigabitEthernet2"
iface_desc="NETCONF_TEST"
ip_addr='10.1.1.1'
netmask_addr='255.255.255.0'

netconf_template = f"""
  <config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>{iface_name}</name>
        <description>{iface_desc}</description>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>{ip_addr}</ip>
            <netmask>{netmask_addr}</netmask>
          </address>
        </ipv4>
      </interface>
    </interfaces>
    </config>
"""


with manager.connect(
        host=ios_xe_host,
        port=ios_xe_port,
        username=ios_xe_username,
        password=ios_xe_password,
        hostkey_verify=False,
        look_for_keys=False
) as m:
    device_reply = m.edit_config(netconf_template, target='running')
    print(device_reply)