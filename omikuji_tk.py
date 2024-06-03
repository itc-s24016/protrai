#s24016
#GUIで動くおみくじプログラム

import tkinter as tk
import random
                    
root=tk.Tk()
root.geometry("200x50")

kuji=["大吉","中吉","小吉","凶","大凶"]

lbl=tk.Label(text=random.choice(kuji))
lbl.pack()

root.mainloop()
