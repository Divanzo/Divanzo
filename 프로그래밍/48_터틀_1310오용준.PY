from turtle import*
import random as r

alist=["red", "blue", "green", "yellow", "purple"]
shape("turtle")
pensize(3)

# color(r.choice(alist))
# for i in range(4):
#     fd(100)
#     lt(90)
# color(r.choice(alist))

# for i in range(3):
#     fd(100)
#     lt(120)

# begin_fill()
# color(r.choice(alist))
# circle(50)
# end_fill()

# penup()
# goto(100, 100)
# pendown()

# for i in range(5):
#     fd(100)
#     lt(72)

n=int(input("정다각형의 변의 개수: "))

penup()
goto(100, 100)
pendown()

color(r.choice(alist))
begin_fill()
for i in range(n):
    m=360/n
    fd(100)
    lt(m)
end_fill()

exitonclick()