from turtle import*
import random as r

tc =Turtle()
tc.shape("turtle")
tc.color("yellow")
tc.up()
tc.speed(0)

tv=Turtle()
tv.shape("turtle")
tv.color("red")
tv.speed(0)
tv.up()
tv.goto(0,200)

tf=Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0,-200)


def turn_right():
    tc.setheading(0)
    
def turn_up():
    tc.setheading(90)

def turn_left():
    tc.setheading(180)
    
def turn_down():
    tc.setheading(270)
    
def play():
    tc.fd(10)
    ang=tv.towards(tc.pos())
    tv.setheading(ang)
    tv.fd(8.5)
    
    if tc.distance(tf)<12:
        start_x=r.randint(-230,230)
        start_y=r.randint(-230,230)
        tf.goto(start_x,start_y)
        
    if tc.distance(tv)>=12:
        ontimer(play,1000)

def ready():
    setup(500,500)
    title("Turtle")
    bgcolor("orange")
   

def move():
    onkeypress(turn_up,"Up")
    onkeypress(turn_left,"Left")
    onkeypress(turn_down,"Down")
    onkeypress(turn_right,"Right")
    onkeypress(play,"space")


ready()
move()
listen()

exitonclick()
