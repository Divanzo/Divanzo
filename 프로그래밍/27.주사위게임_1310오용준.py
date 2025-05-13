import random as r

a,b=map(int, input("2개 입력 (1~6, 중복 허용): ").split())

Mine=[a,b]
dice=list(range(1,7))
Com=r.choices(dice,k=2)

rank=3

if a[0] in Com[0] :
    rank-=1

elif (a[0] in Com) and (a[1] in Com):
    rank-=2

print(f"{rank}등!")
