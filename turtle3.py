#turtle2.py
#カラフルな花
from turtle import *
shape("turtle")
#col=["orange","limegreen","gold","plum","tomato"]
col=["red","blue","green","brown","black"]
for i in range(5):
    color(col[i])
    circle(100)
    left(72)
done()
