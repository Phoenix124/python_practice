from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
import re
from collections import Counter


s = str(html)
regex = '<code>(.*?)</code>'
l = sorted(re.findall(regex, s))
print(Counter(l))
