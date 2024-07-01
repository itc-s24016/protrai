#s24016
#画像を90度回転
import tkinter as tk
import tkinter.filedialog as fd
import PIL.ImageTk

def dispPhoto(path):
    newImage=PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300,300))
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
