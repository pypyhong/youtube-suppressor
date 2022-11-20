import requests
from bs4 import BeautifulSoup

keyword = input('유튜브에서 원하는 정보의 키워드:')


url = "https://www.youtube.com/watch?v=ZDh1C7qw0Rs"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title.get_text())

val = soup.title.get_text().find(keyword)
print(type(soup.title.get_text()))
print(val)

if val != -1:
    print('실행')
else:
    print('실행중지')

