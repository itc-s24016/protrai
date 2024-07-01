#s24016
#dispImage.py
#ファイルマネージャーが開いて選択した画像をウィジェットに表示する
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

root=tk.Tk()
root.geometry("400x350")

btn=tk.Button(text="ファイルを開く",command=openFile)
btn.pack()
imageLabel=tk.Label()
imageLabel.pack()

tk.mainloop()
