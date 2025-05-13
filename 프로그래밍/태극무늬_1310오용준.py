from turtle import *

bgcolor("black")

speed(0)

for i in range(200):
    if i%3==0:
        color("red")
        
    elif i%3==1:
        color("yellow")
    
    else:
        color("blue")
    
    i*=2
    fd(i)
    lt(151)

exitonclick()
