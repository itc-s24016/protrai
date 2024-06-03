#turtle2.py
#カラフルな花
from turtle import *
shape("turtle")

col=["red","yellow"]*15

begin_fill()
for i in range(5*3):
    color(col[i])
    forward(100+i*10)
    right(360/5*2)
end_fill()
done()
