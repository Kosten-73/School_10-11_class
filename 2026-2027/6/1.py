from turtle import *

left(90), pendown(), tracer(0), screensize(2000, 2000)
k = 20
for i in range(3):
    pendown()
    for j in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    penup()
    forward(5 * k)
    right(90)
    forward(5 * k)
    left(90)

for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()
done()
