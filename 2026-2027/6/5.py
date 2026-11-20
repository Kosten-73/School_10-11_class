from turtle import *

left(90), pendown(), tracer(0), screensize(2000, 2000)
k = 10
for _ in range(2):
    forward(17 * k)
    left(90)
    forward(10 * k)
    left(90)
penup()
backward(4 * k)
right(90)
backward(3 * k)
left(90)
pendown()

for _ in range(2):
    forward(40 * k)
    right(90)
    forward(12 * k)
    right(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(2)
done()
