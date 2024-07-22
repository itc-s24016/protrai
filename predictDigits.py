#s24016
#手書きの数字を読み込んで当てる

import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy#数値リストに変換する

def imageToData (filename):#画像ファイルを数値リストに変換する
    #画像を8x8のグレースケール(モザイク)に変換
    grayImage = PIL.Image.open (filename) .convert ("L")
    grayImage = grayImage.resize ( (8, 8), PIL.Image.Resampling.LANCZOS)

    #数値リストに変換
    numImage = numpy.asarray (grayImage, dtype = float)
    numImage = 16 - numpy.floor (17*numImage/256)
    numImage = numImage.flatten()

    print(numImage)
    return numImage

def predictDigits (data) :#数値を予測する
    digits = sklearn.datasets.load_digits()#sklearnで学習データを読み込む
    clf = sklearn.svm.SVC (gamma=0.001)#機械学習をする
    clf.fit (digits.data,digits.target)
    n = clf.predict ([data])#予測結果を出力
    print("予測=",n)

data = imageToData ("tmp/3.png")#画像のパス
predictDigits (data)
