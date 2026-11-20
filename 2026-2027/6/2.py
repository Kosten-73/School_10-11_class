from turtle import *

left(90), pendown(), tracer(0), screensize(2000, 2000)
k = 20
for _ in range(5):
    forward(30 * k)
    right(90)
    forward(40 * k)
    right(90)
penup()
forward(20 * k)
right(90)
forward(5 * k)
right(90)
pendown()

for _ in range(7):
    forward(10 * k)
    right(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot()
done()
