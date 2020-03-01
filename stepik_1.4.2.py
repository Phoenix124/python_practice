import requests
from bs4 import BeautifulSoup

url = 'https://stepik.org/media/attachments/lesson/209723/4.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
answer = 0
for number in soup.find_all('td'):
    try:
        answer += int(str(number).split('>')[1].split('<')[0])
    except:
        try:
            answer += int(str(number).split('>')[2].split('<')[0])
        except:
            try:
                answer += int(str(number).split('>')[3].split('<')[0])
            except:
                pass
print(answer)
