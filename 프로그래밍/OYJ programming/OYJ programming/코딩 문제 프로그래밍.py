# from turtle import*
# import random as r

# tc =Turtle()
# tc.shape("turtle")
# tc.color("yellow")
# tc.up()
# tc.speed(0)

# tv=Turtle()
# tv.shape("turtle")
# tv.color("red")
# tv.speed(0)
# tv.up()
# tv.goto(0,200)

# tf=Turtle()
# tf.shape("circle")
# tf.color("green")
# tf.speed(0)
# tf.up()
# tf.goto(0,-200)


# def turn_right():
#     tc.setheading(0)
    
# def turn_up():
#     tc.setheading(90)

# def turn_left():
#     tc.setheading(180)
    
# def turn_down():
#     tc.setheading(270)
    
# def play():
#     tc.fd(10)
#     ang=tv.towards(tc.pos())
#     tv.setheading(ang)
#     tv.fd(8.5)
    
#     if tc.distance(tf)<12:
#         start_x=r.randint(-230,230)
#         start_y=r.randint(-230,230)
#         tf.goto(start_x,start_y)
        
#     if tc.distance(tv)>=12:
#         ontimer(play,1000)

# def ready():
#     setup(500,500)
#     title("Turtle")
#     bgcolor("orange")
   

# def move():
#     onkeypress(turn_up,"Up")
#     onkeypress(turn_left,"Left")
#     onkeypress(turn_down,"Down")
#     onkeypress(turn_right,"Right")
#     onkeypress(play,"space")


# ready()
# move()
# listen()

# exitonclick()

#=================================================================
# fp={
#     'apple':1500,
#     'banana':1000,
#     'grape':2000,
#     'orange':2000
# }

# n=input()

# if n in fp:
#     print(fp[n])
# else:
#     print("없음")
#=================================================================
# scores={
#     'Alice':(80,90,85),
#     'Bob':(75,85,95),
#     'Charlie':(90,80,85),
# }

# name=input()

# print(f'{name}의 평균은 {sum(scores[name])/3}입니다.')
#=================================================================
# city={
#     'seoul': (2,-1,3,7,12),
#     'busan': (1,0,4,9,13),
#     'incheon': (2,0,4,8,13),
#     'jeju': (2,0,4,9,14),
# }

# name=input()

# print(f'{name}의 기온은 {sum(city[name])/5}도입니다.')
#=================================================================
# products={
#     'Laptop': (1000000,0.1),
#     'Smartphone': (800000,0.15),
#     'Tablet': (600000,0.5)
# }

# name=input()
# price, discount = products[name]

# print(f'{name}의 {price*(1-discount)}입니다.')
#=================================================================
# exchange={
#     ('USD', 'KRW'): 1300,
#     ('EUR', 'KRW'): 1450,
#     ('USD', 'EUR'): 0.9
# }

# n=list(input().split())

# n[0]=int(n[0])

# exchange_rate=exchange[(n[1],n[3])]

# print(exchange_rate*n[0],n[3])
#=================================================================
# while True:
#     n=list(input('이름과 전화번호를 입력하세요(종료:exit): ').split())

#     if n[0]=='exit':
#         break
#     else:
#         Cellphone = {n[0]:n[1]}

# a=input('조회할 이름을 입력하세요: ')

# if a in Cellphone:
#     print(f'{a}의 전화번호는 {Cellphone[a]}입니다.')
#==================================================================




