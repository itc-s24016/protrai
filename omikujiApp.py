#s24016
#omikujiApp.py
import tkinter as tk
import random
def dispLabel():
    lbl.config(text = random.choice(["大吉","中吉","小吉","凶","大凶"]))

root = tk.Tk()
root.geometry("400x200")

lbl = tk.Label(text = "お参り",font = ("Helvetica",20))
btn = tk.Button(text = "投げ銭",command = dispLabel,font = ("Helvetica",20))

btn.pack() # 配置する
lbl.pack() # 配置する
