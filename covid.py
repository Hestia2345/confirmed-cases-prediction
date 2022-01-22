import requests
from bs4 import BeautifulSoup

headers = { "user-Agent": 'Mozilla/5.0 (Macintosh; intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#5일 전 ~ 1일 전 코로나 확진자 데이터 불러오기

d7 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
d6 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(3)')
d5 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(4)')
d4 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(5)')
d3 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(6)')
d2 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(7)')
d1 = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(8)')

down = 0
up = 0

d7 = d7.text.replace(',', '')
d6 = d6.text.replace(",", '')
d5 = d5.text.replace(",", '')
d4 = d4.text.replace(",", '')
d3 = d3.text.replace(",", '')
d2 = d2.text.replace(",", '')
d1 = d1.text.replace(",", '')

#확진자가 상승폭인지 하락폭인지 판단

if int(d6) > int(d7):
    up += 1
else:
    down += 1

if int(d5) > int(d6):
    up += 1
else:
    down += 1

if int(d4) > int(d5):
    up += 1
else:
    down += 1

if int(d3) > int(d4):
    up += 1
else:
    down += 1

if int(d2) > int(d3):
    up += 1
else:
    down += 1

if int(d1) > int(d2):
    up += 1
else:
    down += 1

upordown = 0
if up > down:
    upordown = 1

general_before = (int(d2)-int(d1)) + (int(d3)-int(d2)) + (int(d4)-int(d3)) + (int(d5)-int(d4)) + (int(d6)-int(d5)) + (int(d7)-int(d6))
general = general_before / 5

if upordown == 0:
    general * -1

print(int(d1) + general)