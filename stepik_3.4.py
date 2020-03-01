from os.path import exists

import requests
import xmltodict

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
filename = 'map2.osm'
if not exists(filename):
    with open(filename, 'wb') as f_out:
        f_out.write(requests.get(url).content)

with open(filename, 'r', encoding='utf8') as fin:
    xml = fin.read()

withfuel = 0
parsedxml = xmltodict.parse(xml)

for item in parsedxml['osm']['node']:
    if 'tag' in item:
        tags = item['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == "amenity" and tag['@v'] == "fuel":
                    withfuel += 1
        else:
            if '@k' in tags and tags['@k'] == "amenity" and tags['@v'] == "fuel":
                withfuel += 1
for item in parsedxml['osm']['way']:
    if 'tag' in item:
        tags = item['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == "amenity" and tag['@v'] == "fuel":
                    withfuel += 1
        else:
            if '@k' in tags and tags['@k'] == "amenity" and tags['@v'] == "fuel":
                withfuel += 1
print(withfuel)
