from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
td = soup.find_all('td')
clean = int(str(td).split('>')[1].split('<')[0])
answer = 0
for number in soup.find_all('td'):
    answer += int(str(number).split('>')[1].split('<')[0])

print(answer)
