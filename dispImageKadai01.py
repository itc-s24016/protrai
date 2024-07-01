#s24016
#dispImage.py_ver2
import tkinter as tk
import tkinter.filedialog as fd
import PIL.ImageTk

def dispPhoto(path):
    newImage=PIL.Image.open(path).resize((300,300))
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl.config(text=fpath)

root=tk.Tk()
root.geometry("600x370")

lbl=tk.Label(text="画像表示アプリ バージョン2.0",font=("Helvetica",20))
lbl.pack()

btn=tk.Button(text="ファイルを開く",command=openFile)
btn.pack()

imageLabel=tk.Label()
imageLabel.pack()

tk.mainloop()
