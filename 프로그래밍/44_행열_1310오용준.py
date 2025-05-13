# 44-1
n=int(input())
m=int(input())

for i in range(1,n+1):
    for j in range(1,m+1):
        print(f"{j*i}",end=" ")
    print()

# 44-2
row=int(input())
col=int(input())

for i in range(0,row):
    for j in range(1,col+1):
        print(f"{j+(col*i)}",end=" ")
    print()