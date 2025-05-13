import random as r

while True:
    a=r.randint(1, 10)
    b=r.randint(1, 10)
    
    sum1=0
    
    if a>b:
        for i in range(b, a+1):
            sum1+=i
        print(f"{b}~{a}={sum1}")
    
    elif a<b:
        for i in range(a, b+1):
            sum1+=i
        print(f"{a}~{b}={sum1}")
    
    else:
        print(f"{a}~{b}={a}")
        break