from turtle import*
import random as r

x_min=-5; x_max=5
y_min=-5; y_max=5

space=0.1
speed(3)
pensize(3)

func_list=["x*x","abs(x)","0.5x+1"]

setworldcoordinates(x_min,y_min,x_max,y_max)
up(); goto(x_min,0)
down(); goto(x_max,0)
goto(0,0)
    
up(); goto(0,y_min)
down(); goto(0,y_max)

for i in range(len(func_list)):
    color(r.choice(['red','green','yellow','blue']))
    x=
    y=eval(func_list)

