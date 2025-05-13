
while True:
    a,b=map(int,input().split())
    try:
        c=a/b
        
    except ZeroDivisionError:   
        c=a/b
        print(f"0으로 못나눔: 다시 입력")
    else:
        print(c)