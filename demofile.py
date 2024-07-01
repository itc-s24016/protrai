#s24016
#
import tkinter as tk

root = tk.Tk() # 画面を作る
root.geometry("200x100") # 画面の大きさ

btn = tk.Button(text = "PUSH") # PUSHと描かれたボタンを作る

btn.pack()
tk.mainloop()
