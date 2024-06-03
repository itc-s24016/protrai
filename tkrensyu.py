#GUIで動くアプリを作ってみるよ

import tkinter as tk            #まずこの行を書く必要があるよ


root=tk.Tk()                    #初めのおまじない

root.geometry("800x500")        #ウィンドウのサイズを決める
root.title("ハローアプリ")      #ウィンドウのタイトルを決める
lbl=tk.Label(text="こんにちは世界")#print()のようなもの
lbl.pack()                      #lblを配置させる必要があるよ




root.mainloop()                 #終わりのおまじない
