import yaml
from yaml import load, load_all
from pprint import pprint as pp
# import xml.etree.ElementTree as ET
from lxml import etree as ET
import xmltodict

stream = open('sample.yaml', 'r')
data = load_all(stream, Loader=yaml.FullLoader)

for doc in data:
    pp("New Document")
    pp(doc)
    xx = []
    for key, value in doc.items():
        xx = value

    pp(xx)

stream = open('sample.xml', 'r')
# xml = ET.parse(stream)
#
# root = xml.getroot()
#
# for e in root:
#     pp(ET.tostring(e))
#     # print(e)
#     pp(e.get('Id'))

xml = xmltodict.parse(stream.read())

pp(xml)

for e in xml['People']['Person']:
    pp(e)
    pp(e['Firstname'])


import json

jsonstr = """{
  "People": [
    {
      "id": 1,
      "Firstname": "Aramide",
      "LastName": "Oluwatosin",
      "Email": "aoluwatosin@gmail.com",
      "Active": true
    },
    {
      "id": 1,
      "Firstname": "Aramide",
      "LastName": "Dami",
      "Email": "dfamuyibo@gmail.com"
    }
  ]
}"""


jsonobj = json.loads(jsonstr)
pp(jsonobj["People"][0]['Email'])

jsonobj = json.load(open('sample.json'))
pp(jsonobj["People"][1]['Email'])



