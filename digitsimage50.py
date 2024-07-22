#s24016
#ピクセルの配置で数字を認識する(画像付き)
#明0-16暗
import sklearn.datasets
import matplotlib.pyplot as plt

digits=sklearn.datasets.load_digits()

for i in range(50):
    plt.subplot(5,10,i+1)                                   #5x10に順番に表示する
    plt.axis("off")                                              #枠線を非表示
    plt.title(digits.target[i])                               #この数字は何か
    plt.imshow(digits.images[i],cmap="Greys")
plt.show()
