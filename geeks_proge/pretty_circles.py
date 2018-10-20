from turtle import Turtle, Screen
t = Turtle()
s = Screen()
n = 200
s.colormode(255)
t.speed(0)
s.delay(0)

for i in range(0, 256):
    t.color(i, 0, 0)
    t.circle(n)
    t.right(90)

    n -= 1

s.exitonclick()