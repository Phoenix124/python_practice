import requests
import xmltodict
from os.path import exists
from collections import OrderedDict


url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
filename = 'map2.osm'
if not exists(filename):
    with open(filename, 'wb') as f_out:
        f_out.write(requests.get(url).content)

with open(filename, 'r', encoding='utf8') as f_in:
    xml = f_in.read()

parsedxml = xmltodict.parse(xml)

counter = 0
for node in parsedxml['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, OrderedDict):  # single tag
            tags = [tags]
        for tag in tags:
            if tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                counter += 1
print(counter)
