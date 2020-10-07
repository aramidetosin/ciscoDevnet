# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     breakpoint()
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     print_hi('Tosin')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# def duplicate_count(text):
#     new_dict = {}
#     for i in range(0, len(text)):
#
#         kk = text[i].upper()
#         if new_dict.get(kk) is None:
#             new_dict[kk] = 1
#         else:
#             new_dict[kk] += 1
#
#     count = 0
#     for k, v in new_dict.items():
#         if v >= 2:
#             count += 1
#
#     return count
#
#
# print(duplicate_count('abcde'))
# print(duplicate_count("abcdea"))
# print(duplicate_count("indivisibility"))

import requests
import json
from pprint import pprint as pp
from rich import box, print, table, console
import itertools

m = {
    'ip': '172.16.100.146',
    'port': 443,
    'user': 'cisco',
    'password': 'cisco',
    'hostkey_verify': False,
    'look_for_keys': False
}

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}
interfaces = ['GigabitEthernet1', 'GigabitEthernet2']

url = f"https://{m['ip']}:{m['port']}/restconf/data/ietf-interfaces:interfaces-state"
response = requests.get(url, headers=headers, auth=(m['user'], m['password']), verify=False)
api_data = response.json()
# pp(api_data)
x = api_data['ietf-interfaces:interfaces-state']['interface']
table1 = table.Table(title='Interface utilization', style='blue')
table1.add_column("iface", justify='center', style='green')
table1.add_column("utilization", justify='center', style='red')

if_data = []
for i in x:
    if i['name'] in interfaces:
        # pp(f'ifINutilization for {i["name"]} = {i["statistics"]["in-unicast-pkts"]}')
        if_data.append(i["statistics"]["in-unicast-pkts"])
        # table1.add_row(f'[red]{i["name"]}[/red] = {i["statistics"]["in-unicast-pkts"]}')
for (a, i) in itertools.zip_longest(interfaces, if_data):
    table1.add_row(a,i)

tt = console.Console()
tt.print(table1)

        # mm = lt.Table().csv_import("""\
        # iface,ifaceUtilization
        # [red]{}[/red],{}""".format(i['name'], i['statistics']["in-unicast-pkts"]))
        #
        # mm.present(box=box.SQUARE)
# url = f"https://{m['ip']}:{m['port']}/restconf/data/ietf-interfaces:interfaces-state/interface={iface}/statistics/in-unicast-pkts"
# https://172.16.100.146:443/
#     response = requests.get(url, headers=headers, auth=(m['user'], m['password']),verify=False)
#     api_data = response.json()
#     pp(f"ifINutilization for {iface} = {api_data['ietf-interfaces:in-unicast-pkts']}")
# pp(api_data['ietf-interfaces:interfaces']['interface'])
