# num=1

# while num<=100:
#     print(f"현재숫자는 {num}입니다")
#     num+=1
# print('프로그래밍')


# 2진수 계산기
n=input()
alist=[]
sum1=0

for digit in n:
    digit=int(digit)
    alist.append(digit)

for i in range(len(alist)-1,-1,-1):
    if alist[len(alist)-1-i]==1:
        sum1+=2**i 
    else:
        sum1+=0

print(sum1)

# 2보수 계산기
# n=int(input())
# alist=[]
# Bosoo_value=[1]

# i=0
# sum1=n

# # "10진수->2진수"의 지수 찾기
# while True:
#     if n>2**i:
#         i+=1
#     else:
#         break
    
# for j in range(i-1,-1,-1):
#     if n-2**j>=0:
#         alist.append(1)
#         n-=2**j
#     else:
#         alist.append(0)

# # 1보수로 변환
# for j in range(len(alist)):
#     if alist[j]==1:
#         alist[j]=0
#     else:
#         alist[j]=1

# # 1보수->2보수
# plusung=1

# if alist[-1]==0:
#     alist[-1]=plusung
#     alist[-2]=1

# elif alist[-1]==1:
#     alist[-1]=0

# print(alist)
