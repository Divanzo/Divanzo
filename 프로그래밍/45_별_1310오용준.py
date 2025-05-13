# 45-1
print("== 45-1 ==")
n=int(input())

for i in range(n):
    for j in range(0,i+1):
        print("*", end="")
    print()

# 45-2
print("== 45-2 ==")
n=int(input())

for i in range(n):
    for j in range(i,n):
        print("*", end="")
    print()

# 45-3
print("== 45-3 ==")
n=int(input())

for i in range(n):
    for j in range(i,n-1):
        print(" ", end="")
    for j in range(0,i+1):
        print("*", end="")
    print()

# 45-4
print("== 45-4 ==")
n=int(input())

for i in range(n):
    for j in range(0,i):
        print(" ", end="")

    for j in range(n-i,0,-1):
        print("*", end="")
    print()

# 45-5
print("== 45-5 ==")
n=int(input())

for i in range(n):
    for j in range(i,n-1):
        print(" ", end="")

    for j in range(0,2*i+1):
        print("*", end="")
    print()

# 45-6
print("== 45-6 ==")
a=int(input())
b=int(a/2)+1

for i in range(b):
    for j in range(b-i-1,0,-1):
        print(" ", end="")
    for j in range(0,2*i+1):
        print("*", end="")
    print()

for i in range(b-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range(2*(b-i-1)-1):
        print("*", end="")
    print()
    