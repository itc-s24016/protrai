#s24016
#画像をモノクロに変換
import tkinter as tk
import tkinter.filedialog as fd
import PIL.ImageTk

def dispPhoto(path):#画像を読み込んでグレースケールに変換　
    newImage=PIL.Image.open(path).resize((300,300)).convert("L")
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl2=tk.Label(text=fpath,font=("Helvetica",15))
        lbl2.pack()

root=tk.Tk()
root.geometry("600x400")

lbl=tk.Label(text="画像表示アプリ バージョン2.0",font=("Helvetica",20))
lbl.pack()
btn=tk.Button(text="ファイルを開く",command=openFile)
btn.pack()

imageLabel=tk.Label()
imageLabel.pack()

tk.mainloop()
