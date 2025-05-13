#39-1
n=int(input("자연수 입력: "))
sum1=0
for i in range(1, n+1):
    sum1+=i
print(f"1부터 {n}까지의 합은 {sum1}입니다.")

#39-2
n=int(input("자연수 입력: "))
sum2=1
for i in range(1, n+1):
    sum2*=i
print(f"1부터 {n}까지의 합은 {sum2}입니다.")

