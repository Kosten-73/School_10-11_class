from turtle import *

left(90), pendown(), tracer(0), screensize(20000, 20000)
k = 10

# for _ in range(3):
#     pendown()
#     for _ in range(2):
#         forward(10 * k)
#         right(90)
#         forward(10 * k)
#         right(90)
#     penup()
#     forward(5 * k)
#     right(90)
#     forward(5 * k)
#     left(90)
#
# penup()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         setpos(x * k, y * k)
#         dot()
# done()


# for _ in range(5):
#     forward(30 * k)
#     right(90)
#     forward(40 * k)
#     right(90)
# penup()
# forward(20 * k)
# right(90)
# forward(5 * k)
# right(90)
# pendown()
# for _ in range(7):
#     forward(10 * k)
#     right(90)
#
# penup()
# for x in range(-70, 50):
#     for y in range(-50, 50):
#          setpos(x * k, y * k)
#          dot(2)
# done()

# for _ in range(7):
#     forward(12 * k)
#     right(90)
#     fd(20 * k)
#     rt(90)
# up()
# fd(1 * k)
# right(90)
# fd(10 * k)
# lt(90)
# down()
# for i in range(7):
#     fd(66 * k)
#     rt(90)
#     fd(92 * k)
#     rt(90)
# penup()
#
# for x in range(-70, 50):
#     for y in range(-50, 50):
#         setpos(x * k, y * k)
#         dot(3)
# done()

for _ in range(2):
    forward(17*k), left(90), forward(10*k), left(90)
penup()
backward(4*k),right(90), backward(3*k),left(90)
pendown()
for _ in range(2):
    forward(40*k), right(90), forward(10*k), right(90)
penup()

for x in range(-70, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)
done()