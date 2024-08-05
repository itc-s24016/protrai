#s24016
#沖縄県の推計人口のホームページから最新情報をスクレイピングするプログラム（途中）
import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

#文字コードをShift_JISにエンコーディング
html.encoding = "Shift_JIS"

soup = BeautifulSoup(html.text, 'html.parser')

#タイトルを取得＆出力
print(soup.find("title").string)

#tableタグのtable1 font2 gyo5クラスをHTML全体から抜き取る
my_data = soup.find('table', class_='table1 font2 gyo5')

print(my_data.find_all(''))
