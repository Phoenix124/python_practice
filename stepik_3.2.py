import requests
import xmltodict
from os.path import exists


url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
filename = 'map1.osm'
if not exists(filename):
    with open(filename, 'wb') as f_out:
        f_out.write(requests.get(url).content)

with open(filename, 'r', encoding='utf8') as f_in:
    xml = f_in.read()

parsedxml = xmltodict.parse(xml)

with_tag_count = sum('tag' in node for node in parsedxml['osm']['node'])
without_tag_count = len(parsedxml['osm']['node']) - with_tag_count
print(f'{with_tag_count} {without_tag_count}')
