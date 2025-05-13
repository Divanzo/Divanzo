def fun_f(n):
    if n==1:
        return 1
    else:
        return n*fun_f(n-1)

def fun_s(n2):
    sum1=0
    if n2==1:
        return 1
    else:
        return n2+fun_s(n2-1)

print(fun_s(1))
print(fun_s(10))
b=int(input("정수 입력: "))
print(fun_s(b))

print(fun_f(1))
print(fun_f(10))
a=int(input("정수 입력: "))
print(fun_f(a))