#s24016
#時間を表示させる「時計アプリ」
#時計アプリを使いやすくするためにバージョンアップしていきます

import datetime
import tkinter as tk #GUIでアプリを作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime(" %Y年%m月%d日 %H時%M分%S秒  ")  #printではなく変数に入れている

    lbl.config(text = current_time)
    root.after(1000,update_time)


#tkinterのウィンドウを作成
root = tk.Tk()#初めの文言

root.title("⏰現在の時刻⏰")
lbl = tk.Label()
lbl.config(text = "", font=("Helvetica", 67))
lbl.pack()  #packすることでウィンドウ内にラベルをいれる

#関数の呼び出し
update_time()

root.mainloop()#終わりの文言
