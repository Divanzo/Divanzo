# def main():
#     n=int(input(""))
#     sum1=1
    
#     for i in range(1,n+1):
#         sum1*=i
#     print(sum1)
# main()

# n,m=input().split()
# n=int(n)
# m=int(m)

# if n!=m:
#     print("True")
# else:
#     print("False")

# 등차수열 문제
# a,d,n=map(int, input().split())

# print(a+d*(n-1))

#역순 별찍기
# a=int(input())

# for i in range(0,a):
#     for j in range(0,i):
#         print("_",end="")
#     for j in range(a-i,0,-1):
#         print("*",end="")
#     print("\n")

# # 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)
# a,m,d,n=map(int, input().split(' '))
# sum1=a

# for i in range(0,n-1):
#     sum1*=m
#     sum1+=d

# print(sum1)


# 리스트에 곱하기하여 출력하면 리스트하나에 복사되어 출력 가능
# n,m=map(int, input().split(' '))
# alist=[]
# blist=[]

# for i in range(0,n):
#     alist.append(i+1)
# blist=alist*m
# print(blist)

#순차 별찍기
# n=int(input())

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\n")


# 직사각형 입력
# n,m=map(int, input().split(' '))
# alist=[]
# blist=[]
# num=0
# Index_=0

# #숫자 모아둔 리스트
# for i in range(1,n*m+1):
#     blist.append(i)
# #1~n*m까지의 수들을 2차원배열로 만들어둔 리스트
# for i in range(1,n+1):
#     row=[]
#     for j in range(1,m+1):
#         num+=1
#         row.append(num)    
#     alist.append(row)
# #행->열 차례로 만들어낸 반복문
# for j in range(0,m):    
#     for i in range(0,n):
#         if Index_<=11:    
#             alist[i][j]=blist[Index_]
#             Index_+=1
# #역순으로 정리한 포문 두개
# # for i in range(0,n):
# #     alist[i].sort(reverse=True)

# # alist.sort(reverse=True)

# # # 사각형 형태 출력
# for row in alist:
#     print(row)

#문제(지렁이 배열)

#1 6 7
#2 5 8
#3 4 9

# n,m=map(int, input().split(' '))
# alist=[]
# blist=[]
# num=0
# num1=0

# for i in range(1,n+1):
#     row2=[]
#     row1=[]
#     for j in range(1,m+1):
#         num1+=1
#         num+=1
#         row2.append(num1)    
#         row1.append(num)
#     blist.append(row2)
#     alist.append(row1)
# # [1,2,3]
# # [4,5,6]
# # [7,8,9]

# for i in range(0,n):
#     for j in range(i,m):
#         alist[i][j],alist[j][i]=alist[j][i],alist[i][j]
#         blist[i][j],blist[j][i]=blist[j][i],blist[i][j]
# # [1,4,7]
# # [2,5,8]
# # [3,6,9]

# blist.sort(reverse=True)


# for i in range(0,n):
#     for j in range(0,n):    
#         if j>0 and j%2!=0:
#             alist[i][j]=blist[i][j]

# for row in alist:
#     print(row)

# 정사각형 만들기 (치환 및 대입)
# def snake(n):
#     alist=[]
#     blist=[]
#     Index_=[]
#     num1=0

#     # 1~n*n 사각형 만드는 for문 식
#     for i in range(1,n*n+1):
#         Index_.append(i)

#     # 빈정사각형
#     for i in range(0,n):
#         row=[]
#         for j in range(1,n+1):
#             row.append(0)
#         alist.append(row)
    
#     for j in range(n):
#         for i in range(n):
#             if j>0 and j%2!=0:
#                 alist[len(alist[0])-1-i][j]=Index_[num1]
#             else:
#                 alist[i][j]=Index_[num1]
#             num1+=1
        
#     return alist

# def main():
#     n=int(input())

#     for row1 in snake(n):
#         print(row1)
# main()

# # 직사각형 지렁이 배열 만들기(뒤집기 및 대입 or 치환 가능)
# n, m = map(int, input().split())
# Index_=[]
# num1=0
# alist=[]
# ig=0
# # plusing nums
# for i in range(1,n*m+1):
#     Index_.append(i)

# #madin 2d array
# for i in range(n):
#     row=[]
#     for j in range(m):
#         num1+=1
#         row.append(0)
#     alist.append(row)

# #work for Ce
# for i in range(len(alist)-1,-1,-1):
#     for j in range(len(alist[0])-1,-1,-1):
#         if i>0 and i%2!=0:
#             alist[i][j]=Index_[ig]
#         else:
#             alist[i][j]=Index_[ig]
#         ig+=1

# for i in range(n):
#     for j in range(m):
#         if i>0 and i%2!=0:
#             alist[i].sort()
            
# for row in alist:
#     print(row)

#2차원 누적합
    #치환 및 대입 and reverse=True
    # n, m = map(int, input().split())
    # Index_=[]
    # num1=0
    # alist=[]
    # # made 1*m nums
    # for i in range(1,m+1):
    #     Index_.append(i)

    # #madin 2d array
    # for i in range(n):
    #     row=[]
    #     for j in range(m):
    #         num1+=1
    #         row.append(0)
    #     alist.append(row)

    # #work for Ce
    # for i in range(0,n):
    #     for j in range(0,m):
    #         alist[i][j]=Index_[j]

    # #change the order
    # for i in range(0,n):
    #     for j in range(0,m):
    #         if i>0 and i%2!=0:
    #             alist[i].sort(reverse=True)

    # #the result
    # for row in alist:
    #     print(row)
#=============================================================
# n,m=map(int, input().split())
# alist=[]
# nums=[]
# # 3 5
# # 1 2 3 4 5
# # 5 4 3 2 1
# # 1 4 2 5 3

# #입력하고 나서 바로 수 넣기
# for i in range(0,n):
#     a,b,c,d,e=map(int, input().split())
#     nums=[a,b,c,d,e]
#     alist.append(nums)

# # for i in range(1,n+1):
# #     for j in range(1,n+1):
        
# for row in alist:
#     print(row)
#==============================================================

# n,m=map(int, input().split())
# alist=[]
# plusing=[]
# Index_=0

# for i in range(1,n*m+1):
#     plusing.append(i)

# for i in range(n):
#     row=[]
#     for j in range(m):
#         row.append(0)
#     alist.append(row)

# for i in range(len(alist)):
#     for j in range(len(alist[0])):
#         if Index_<n*m:
#             if j>0 and j%2!=0:
#                 alist[i][j]=plusing[Index_]
#             else:
#                 alist[i][j]=plusing[Index_]
#             Index_+=1
#     if i>0 and i%2!=0:
#         alist[i].sort()
#     else:
#         alist[i].sort(reverse=True)

# alist.sort(reverse=True)

# for row in alist:
#     print(row)

# =================================================================
#==================================================================
#5*5 세상안에서 섬찾기
# [1, 1, 0, 0, 0]
# [1, 1, 0, 0, 0]
# [0, 0, 0, 1, 1]
# [1, 1, 0, 0, 1]
# [0, 0, 0, 0, 1]

# def finding_top(n,x,y):
#     for x in range(0,n):
#         for y in range(0,n):
#             if alist[x][y]==1:
#                 return n,x-1,y
#             else:
#                 return 0

# def finding_bottom(n,x,y):
#     for x in range(n-1,-1,-1):
#         for y in range(n-1,-1,-1):
#             if alist[x][y]==1:
#                 return n,x+1,y
#             else:
#                 return 0

# def finding_left(n,x,y):
#     for x in range(0,n):
#         for y in range(0,n):
#             if alist[x][y]==1:
#                 return n,x,y-1
#             else:
#                 return 0

# def finding_right(n,alist):
#     for x in range(n-1,-1,-1):
#         for y in range(n-1,-1,-1):
#             if alist[x][y]==1:
#                 return n,x,y+1
#             else:
#                 return 0
# def island(x,y):
#     if alist[x][y]==1:
#         return island(x-1,y)
#         return island(x+1,y)
#         return island(x,y-1)
#         return island(x,y+1)
#     else:
#         return 0

# def main():
#     n=int(input())
#     alist=[]
    
#     for i in range(n):
#         row=[]
#         a,b,c,d,e=map(int, input().split())
#         row.append(a)
#         row.append(b)
#         row.append(c)
#         row.append(d)
#         row.append(e)
#         alist.append(row)
#     for x in range(0,n):
#         for y in range(0,n):
#             alist(x,y)
#     # for row in :
#     #     print(row)

# main()


#문자열 문제
# students_score=[['0',"상민","창익","동현","동욱","예주","혜진"],
#                 ["c언어",100,90,50,60,90,100],
#                 ["java",90,80,90,100,100,100,60],
#                 ["python",80,60,100,90,90,80]]

# for i in range(4):
#     for j in range(7):
#         if 83>=students_score[i][j]:
#             print(students_score[i][j],end=" ")

# for i in range(4):
#     for j in range(7):
#         if i==1 and 100==students_score[i][j]:
#             print("c언어",'=',students_score[i][j],end=" ")

# # 2진수 계산기
# n=input()
# alist=[]
# sum1=0

# for digit in n:
#     digit=int(digit)
#     alist.append(digit)

# for i in range(len(alist)-1,-1,-1):
#     if alist[len(alist)-1-i]==1:
#         sum1+=2**i 
#     else:
#         sum1+=0

# print(sum1)

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

# alist=[]
# blist=[]

# n=int(input())

# for i in range(n):
#     alist=[]
#     alist=list(map(int, input().split()))
#     blist.append(alist)

# print(blist)

# #Finding island
# Island=[[1, 0, 0, 1, 1],
#        [0, 0, 1, 1, 1],
#        [1, 1, 0, 0, 0],
#        [0, 0, 1, 0, 1]]

# Check_Island=[[0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0]]

# fruits=["apple","banana","grape"]

# for index, value in enumerate(fruits):
#     print(index, value)

# aset,bset=map(set, input().split())

# cset=set(aset)&set(bset)

# print(cset)

# capitals={"Korea":"Seoul", "USA":"Washington", "UK":"London"}
# if "UK" in capitals:
#     capitals.pop("UK")

# print(capitals)
# print(capitals.get("Korea","해당키가없습니다."))

# for key in sorted(capitals.keys()):
#     print(key,end="")

#############딕셔너리
# stu1={'학반':105,'연락처':'010-1111-2222','동아리':'파이썬 동아리'}

# question=input("삭제할 정보가 뭐죠?:")

# print(f"정보삭제요청 수락: {stu1[question]}")
#         #======================================================
# del stu1['연락처']
# print(stu1)

# stu1['동아리'] = '연극 동아리'

# print(stu1)

## 연락처 찾기

# while True:
#     print("1. 연락처추가 ")
#     print("2. 연락처삭제 ")
#     print("3. 연락처검색 ")
#     print("4. 연락처출력 ")
#     print("5. 종료")

#     n=int(input("항목 선택: "))

#     if n==1:
#         name=input("이름: ")
#         phone_number=input("전화번호: ")
        
#         store={name:phone_number}
#         ##store[input("이름")]=input("전화번호")

#     elif n==2:
#         name=input("이름 재확인: ")
#         store.pop(name)
        
#         print(store)

#     elif n==3:
#         name=input("이름 입력")
#         print(name,',',store.get(name, "확인 실패"))

#     elif n==4:
#         print(store)

#     elif n==5:
#         print("종료합니다.")
#         break


# ### 거스름돈
# a, b = map(int, input().split())

# change = b - a

# coins = [1000, 500, 100, 50, 10]

# for coin in coins:
#     count = change // coin
#     change %= coin
#     print(f"{coin}원: {count}")



# Island=[[1, 0, 0, 1, 1],
#         [0, 0, 1, 1, 1],
#         [1, 1, 0, 0, 0],
#         [0, 0, 1, 0, 1]]

# Check_Island=[[0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0]]

# nums_of_Island=0

# def main(x,y):
#     #인덱스 초과 및  1체크 복수체크 방지
#     if x<0 or x>len(Island)-1 or y>len(Island[0])-1 or y<0 or Check_Island[x][y]==1 or Island[x][y]==0:
#         return
    
#     Check_Island[x][y]=1

#     #상하좌우 확인

#     main(x-1,y)
#     main(x+1,y)
#     main(x,y+1)
#     main(x,y-1)
#     #체크


#     #모두 확인 후 남은 1의 집합들을 하나로 보고 1로 더해 섬개수 구하기
# for i in range(len(Island)):
#     for j in range(len(Island)-1):
#         if Island[i][j]==1 and Check_Island[i][j]==0:
#             nums_of_Island+=1
#             main(i,j)

# print(nums_of_Island)

# fruit_prices={
#     "apple":1500,
#     "banana":1000,
#     "grape":2500,
#     "orange":2000
# }

# NameOfFruit=input("과일 이름을 입력하시오:")

# print(fruit_prices[NameOfFruit])

# scores={
#     "Alice":(80,90,85),
#     "Bob":(75,85,95),
#     "Charlie":(90,80,85)
# }

# name=input("학생 이름")

# print(f"{name}의 평균 점수는 {sum(scores[name])/3}")

# city_temperature={
#     "Seoul":(2,-1,3,7,12),
#     "Busan":(5,3,8,10,15),
#     "Jeju":(8,6,12,14,18)
# }

# city=input("도시이름: ")

# print(f"{sum(city_temperature[city])/len(city_temperature[city])}도")

# products={
#     "Laptop":(1000000,0.1),
#     "Smartphone":(800000,0.15),
#     "Tablet":(6000000,0.05)
# }

# name=input("상품 이름:")

# print(f"{products[name][0] * (1-products[name][1])}")

# sum1=0
# sum2=0
# sum3=0

# alist=list(input().split())

# for i in range(0,len(alist)):
#     if alist[i]=='apple':
#         sum1+=1

#     elif alist[i]=='banana':
#         sum2+=1

#     else:
#         sum3+=1

# print("apple:",sum1)
# print("banana:",sum2)
# print("orange:",sum3)

# #apple banana apple orange banana apple

# exchange_rates={
#     ("USD","KRW"):1300,
#     ("EUR","KRW"):1450,
#     ("USD","EUR"):0.9
# }

# exchanged=list(input("변환할 금액과 통화: ").split())

# result=exchange_rates[(exchanged[1],exchanged[3])]

# print(f"{result*int(exchanged[0])}")

# location_data={
#     (37.5665,126.9780):"Seoul",
#     (35.1796,129.0756):"Busan",
#     (35.6895,139.6917):"Tokyo"
# }
# #37.5665 126.9780
# Info=list(input("좌표를 입력하세요:").split())

# Info[0]=float(Info[0])
# Info[1]=float(Info[1])

# print(f"{location_data[(float(Info[0]),float(Info[1]))]}")

# alloflists={}
# name=0
# result=0

# while True:
#     name_or_score=list(input("추가할 학생의 이름과 점수를 입력하세요(종료: exit): ").split())
    
#     if name_or_score[0]=='exit':
#         print('종료')
#         break
    
#     else:
#         for i in range(len(name_or_score)):    
#             alloflists[(name_or_score[1],name_or_score[2],name_or_score[3])]=name_or_score[0]
#         find=input('조회할 학생의 이름을 입력하시오:')

#         # if alloflists[find]=
#         for j in range(1,len(name_or_score)):
#             name_or_score[j]=int(name_or_score[j])
#             result+=name_or_score[j]
        
#         result/=3

#         print(f"{find}의 평균점수는 {result}입니다.")

# a=int(input())
# alist=input().split()
# blist=[]

# for i in range(a):
#     alist[i]=int(alist[i])

# for i in range(24):
#     blist.append(0)

# for i in range(a):
#     blist[alist[i]]+=1

# for i in range(1,24):
#     print(blist[i],end=" ")

# d = [[0 for j in range(19)] for i in range(19)]

# n=int(input())

# for k in range(n):
#     a,b=map(int, input().split())

#     for i in range(19):
#         for j in range(19):
#                 if d[i][j]==d[a-1][b-1]:
#                     d[i][j]=1

# for i in range(19):
#     for j in range(19):
#         print(d[i][j],end=" ")
#     print()

# n=int(input())

# sum1=n
# count=0

# for i in range(n): 
#     sum1-=i
#     count+=1
#     if sum1==0:
#         print(count-1)

# n=int(input())

# for i in range(n):
#     for j in range(2,i,-1):
#         print("_",end="")
        
#     for k in range(2*i+1):
#         print("*",end="")
#     print("\n")

# import math as m

# T=int(input())
# test_cased=[]

# for _ in range(T):
#     x1,y1,r1,x2,y2,r2=map(int, input().split())
#     test_cased=[x1,y1,r1,x2,y2,r2]

# # 두 영웅 사이의 거리
#     location=m.sqrt((x2-x1)**2+(y2-y1)**2)

#     r_sum=r1+r2
#     r_diff=r1-r2

#     result=[]

#     if location==0:
#         if r1!=r2:
#             result.append(0)
#         else:
#             result.append(-1)

#     elif location==r_sum:
#         result.append(1)

#     elif r_sum>location:
#         result.append(0)

#     elif location>0 and r_sum==location:    
#         result.append(1)

#     elif r_diff==location:
#         result.append(1)

#     else:
#         result.append(2)

# for BO in result:
#     print(BO)


# arr=[]
# store_list=[]
# N=int(input())

# for _ in range(N):
#     num=int(input())
#     arr.append(num)

# arr.sort()

# M=int(input())

# for i in range(N):
#     if i%M==0 and i!=0:
#         store_list.append(arr[i])

# print(sum(store_list))

# N=int(input())
# M=int(input())

# total_location=[]
# watering_can=[[0]*N for _ in range(N)]

# for i in range(M):
#     x,y,z=map(int,input().split())

#     for i in range(N):
#         for j in range(N):
#             if watering_can[i]==x and watering_can[j]==y:
#                 watering_can[i][j]=1


# for row in watering_can:
#     print(row)


# n=int(input())
# result=0
# b=[]

# for i in range(n):
#     a=input()
#     b=a.replace("for", "!")
#     c=b.replace("while", "!")
#     if c.count('!')>result:
#         result=c.count('!')

# print(result)

n=int(input())
m=int(input())
void_list=[[0,0,0,0,0] for _ in range(n)]

check_input_list=[]

for i in range(m):
    now_input=[]
    
    x,y,z=map(int, input().split())
    
    now_input.append(x)
    now_input.append(y)
    now_input.append(z)
    
    check_input_list.append(now_input)
    
    void_list[x][y]=1
    
    for i in range(n):
        for j in range(n):
            for distance in range(z):
                if void_list[i][j]==1:
                    if void_list[i+distance][j]==0:
                        void_list[i+distance][j]=1
                    
                    if void_list[i][j+distance]==0:
                        void_list[i][j+distance]=1
                    
                    if void_list[i-distance][j]==0:
                        void_list[i-distance][j]=1
                    
                    if void_list[i][j-distance]==0:
                        void_list[i][j-distance]=1
                
# for i in range(n):
#     for j in range(n):
#         for k in range(0,m):
#             if void_list[i][j]==check_input_list[k][0] and void_list[i][j]==check_input_list[k][1]:
#                 void_list[i][j]=1

#             else:
#                 void_list[i][j]=0


for row in void_list:
    print(row)