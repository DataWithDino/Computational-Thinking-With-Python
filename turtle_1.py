from turtle import *

t = Turtle()
t.color('red', 'yellow')
t.speed(0)
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1: break
t.end_fill()
done()

