#s24016
#app1.py
#押せるボタンを表示
import tkinter as tk

root = tk.Tk() # ウィンドウを作成
root.geometry("200x100") # 画面の大きさ

lbl = tk.Label(text = "LABEL") #  表示するテキストを決める
btn = tk.Button(text = "PUSH") # PUSHと描かれたボタンを作る

lbl.pack() # 配置する
btn.pack() # 配置する
tk.mainloop() # ウィンドウを表示
