#s24016
#app2.py
#app1.pyをバージョンアップしたもの
import tkinter as tk

def dispLabel():
    lbl.config(text = "こんにちは！")

def dispLabel2():
    lbl.config(text = "Hello!")

root = tk.Tk() # ウィンドウを作成
root.geometry("400x200") # 画面の大きさ

lbl = tk.Label(text = "LABEL",font = ("Helvetica",20)) #  表示するテキストを決める
btn = tk.Button(text = "PUSH",command = dispLabel,font = ("Helvetica",20)) # PUSHと描かれたボタンを作る

btn.pack() # 配置する
lbl.pack() # 配置する
lbl2 = tk.Label(text = " Label2",font = ("Helvetica",20)).pack()
btn2 = tk.Button(text = "何もしないボタン",command = dispLabel2,font = ("Helvetica",20)).pack()
tk.mainloop() # ウィンドウを表示
