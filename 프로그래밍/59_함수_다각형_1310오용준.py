from turtle import*

def moving():
    a,b=map(int, input("이동할 좌표(x,y): ").split())

    goto(a,b)

def polygon():
    x,y=map(int, input('종류(3이상) 한 변길이(5이상): ').split())
    
    for i in range(x):
        m=360/x
        fd(y)
        lt(m)
    return

speed(0)

while True:
    print('=== 도형그리기 ===')
    moving()
    polygon()

    con=int(input('계속(1)-아니오(그 외): '))
    if con!=1:
        break

exitonclick()