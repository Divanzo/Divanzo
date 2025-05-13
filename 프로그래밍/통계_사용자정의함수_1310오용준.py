def alist():
    a,b=map(int,input("두 수 입력: ").split())
    lst=list(range(a,b+1))

    return lst

def mean(a):
    return sum(a)/len(a)

#=============================

def var(b):
    vsum=0
    for x in b:
        vsum+=(x-mean(b))**2
    return vsum/len(b)

#=============================

def std(c):
    return math.sqrt(var(c))

#=============================

def gcd(d):
    return math.gcd(*d)

def lcm(e):
    return math.lcm(*e)

#=============================

import math

print(f"두 수의 평균: {mean(alist())}")
print(f"두 수의 분산: {var(alist())}")
print(f"두 수의 표준편차: {std(alist()):.2f}")
print(f"두 수의 최소공약수: {gcd(alist())}")
print(f"두 수의 최소공배수: {lcm(alist())}")
