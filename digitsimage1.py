#s24016
#ピクセルの配置で数字を認識する(画像付き)
#明0-16暗
import sklearn.datasets
import matplotlib.pyplot as plt

digits=sklearn.datasets.load_digits()

plt.imshow(digits.images[0],cmap="Greys")
plt.show()
