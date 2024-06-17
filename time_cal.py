#s24016
#現在時刻と2024/6のカレンダーを表示するプログラム
import calendar
import datetime

now=datetime.datetime.now()
print(now.strftime("--%Y年%m月%d日 (%H:%M:%S)--"))
print(calendar.month(2024,6))
