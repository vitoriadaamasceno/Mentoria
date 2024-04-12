import turtle
bob = turtle.Turtle()

def square(t,lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

#square(bob,400)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#polygon(bob, 7, 70)
import math   
def circle(t,r):
    circun = 2*math.pi *r
    n=50
    length = circun/2
    polygon(t,n,length)

circle(bob,5)