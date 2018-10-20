from turtle import Screen,Turtle


def fraktal(tase, pikkus):
    if tase >= 1:
        t.forward(pikkus)
        t.left(90)
        fraktal(tase-1,pikkus*0.7)
        t.right(180)
        fraktal(tase-1,pikkus*0.7)
        t.left(90)
        t.backward(pikkus)


t=Turtle()
s=Screen()

t.speed(0)
s.delay(0)

fraktal(15,100)
s.exitonclick()
