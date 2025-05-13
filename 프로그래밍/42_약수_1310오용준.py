# 42-1
n=int(input("어떤 수의 약수?: "))

for i in range(1, n+1):
    if n%i==0:
        print(i)

# 42-2
n=int(input("어떤 수의 약수?: "))

for i in range(n,0,-1):
    if n%i==0:
        print(i)