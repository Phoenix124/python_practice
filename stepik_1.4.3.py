from urllib.request import urlopen
from bs4 import BeautifulSoup


def load(url):
    resp = urlopen(url)
    return str(resp.read().decode('utf8'))


html = load('https://stepik.org/media/attachments/lesson/209723/5.html')
soup = BeautifulSoup(html, 'html5lib')
answer = sum(int(td.text.strip()) for td in soup.find_all('td'))
print(answer)
