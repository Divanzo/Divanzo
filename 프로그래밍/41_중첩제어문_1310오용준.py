n=int(input("어떤 수의 배수?: "))

for i in range(50,101):
    if i%n==0:
        print(i)
