from turtle import Screen,Turtle

s=Screen()
t=Turtle()

def fraktal(tase,pikkus):
    if tase >=1:
        t.forward(pikkus)
        t.backward(pikkus/2)
        t.left(90)
        fraktal(tase-1,pikkus*0.71)

fraktal(20,400)
s.delay(0)
t.speed(1)
s.exitonclick()

"""
# Kochi kõver
s=Screen()
t=Turtle()

t.speed(0)
def koch(tase,pikkus):
    if tase == 0:
        t.forward(pikkus)
    else:
        koch(tase-1,pikkus/3)
        t.left(90)
        koch(tase-1,pikkus/3)
        t.right(90)
        koch(tase-1,pikkus/3)
        t.right(90)
        koch(tase-1,pikkus/3)
        t.left(90)
        koch(tase-1,pikkus/3)
koch(5,1000)
s.delay(0)
t.speed(0)
s.exitonclick()
"""