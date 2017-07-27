import json, time, datetime
from datetime import date

from bs4 import BeautifulSoup
from urllib.request import urlopen

# 타학교에서 이용시 수정
regioncode = 'jbe.go.kr'
schulcode = 'P100000429'

# NEIS에서 파싱
html = urlopen(
    'http://stu.' + regioncode + '/sts_sci_md01_001.do?schulCode=' + schulcode + '&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2')
source = html.read()
html.close()

# beautifulsoup4를 이용해 utf-8, lxml으로 파싱
soup = BeautifulSoup(source, "lxml", from_encoding='utf-8')

# div_id="contents"안의 table을 모두 검색 후 td태그만 추출
table_div = soup.find(id="contents")
tables = table_div.find_all("table")
menu_table = tables[0]
td = menu_table.find_all('td')

# 요일 import, 월요일 ~ 일요일 = 0~6
today = datetime.datetime.today().weekday()
print (today)

today = 2

# 월요일 ~ 일요일 = td[8] ~ td[14]
if today == 6:
    menu = '일요일은 급식이 제공되지 않습니다....'
else:
    menu = td[today + 8]

print (menu)

# 파싱 후 불필요한 태그 잔해물 제거
menu = str(menu).replace('*', '').replace('<td', "").replace('<br/></td>', "").replace('class="textC last">', '').replace('class="textC">','').replace('<br/>', '\n').replace('1.', '').replace('2.', '').replace('3.', '').replace('4.', '').replace('5.', '').replace('6.','').replace('7.', '').replace('8.', '').replace('9.', '').replace('10.', '').replace('11.', '').replace('12.', '').replace('13.', '').replace('14.', '').replace('15.', '').replace('1', '').replace(' ', '')

if menu == '':
    menu = '밥이 없습니다. 급식이 없는 날일 수 있으니 확인 바랍니다.'

print (menu)