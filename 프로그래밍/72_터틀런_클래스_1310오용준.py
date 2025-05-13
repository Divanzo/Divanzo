from turtle import*
import random as r

score=0
playing=False

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

def start():
    global playing
    if playing==False:
        playing=True
        clear()
        play()

def play():
    global score
    global playing

    tc.fd(10)
    ang=tv.towards(tc.pos())
    tv.setheading(ang)
    tv.fd(9)
    
    if tc.distance(tv)<12:
        text=(f'score : {score}')
        msg("Game Over", text)
        playing=False
        score=0

    if tc.distance(tf)<12:
        score+=1
        tc.write(score)
        start_x=r.randint(-230,230)
        start_y=r.randint(-230,230)
        tf.goto(start_x,start_y)

    if playing:
        ontimer(play,100)

def msg(m1,m2):
    clear()
    tc.up()
    tc.goto(0,100)
    tc.down()
    tc.write(m1,False,"center",("",20))
    tc.goto(0,-100)
    tc.write(m2,False,"center",("",15))
    home()

def ready():
    setup(500,500)
    title("Turtle")
    bgcolor("orange")

def move():
    onkeypress(turn_up,"Up")
    onkeypress(turn_left,"Left")
    onkeypress(turn_down,"Down")
    onkeypress(turn_right,"Right")
    onkeypress(start,"space")

ready()
move()
listen()
msg("Turtle run","[space]")
exitonclick()

