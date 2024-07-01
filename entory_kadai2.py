#s24016
#入力値を出力するアプリ
import tkinter as tk #tkinterをtkと略する

def name():
    a=entry.get()  #a=input()と同じ意味
    a=int(a)
    lbl.config(text=f"「{a}さん」こんにちは")
    
root=tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")

lbl=tk.Label(text="ラベル",font=("Helvetica",20))
lbl.pack()

entry=tk.Entry(font=("Helvetica",20))  #エントリー=input()
entry.pack()

btn=tk.Button(text="ボタン",font=("Helvetica",13),command=name)
btn.pack()

tk.mainloop()
