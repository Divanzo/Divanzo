# n=int(input())

# result=0

# alist=list(map(int, input().split()))

# for i in range(len(alist)):
#     result+=alist[i]/max(alist)*100

# print(result/n)
#==================================================================
# word=input()
# n=int(input())
# alist=[]

# for i in word:
#     alist.append(i)

# print(alist[n-1])

# n=int(input())

# word=input()
# sum1=0

# for i in word:
#     sum1+=int(i)

# print(sum1)
#=================================================================
# alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# s=input()

# for i in alpha:
#     if i in s:
#         print(s.index(i),end=' ')
#     else:
#         print(-1,end=' ')
#=================================================================
# n=int(input())

# for i in range(n):
#     alist=[]
#     num_word=list(map(str, input().split()))

#     num_word[0]=int(num_word[0])

#     for j in num_word[1]:
#         for k in range(num_word[0]):
#             alist.append(j)
#     for j in alist:
#         print(j,end='')
#     print()
#=================================================================
# word=input().split()

# print(len(word))

# word=input().split()

# for i in range(len(word)):
#     word[i]=int(word[i][::-1])

# print(max(word))
#=================================================================
# diar=[['none'],['none'],[1],[2,'A','B','C'],[3,'D','E','F'],[4,'G','H','I'],[5,'J','K','L'],[6,'M','N','O'],[7,'P','Q','R','S'],[8,'T','U','V'],[9,'W','X','Y','Z'],[0]]
# word=input()
# sum1=0
# for i in word:
#     for j in diar:
#         if i in j:
#             sum1+=diar.index(j)

# print(sum1)
#=================================================================
# import sys

# for line in sys.stdin:
#     print(line.strip())

# info=[1,1,2,2,2,8]
# Check=[]

# alist=list(map(int, input().split()))

# for i in range(len(info)):
#     if info[i]==alist[i]:
#         Check.append(0)
#     elif info[i]>alist[i] or info[i]<alist[i]:
#         Check.append(info[i]-alist[i])

# for i in Check:
#     print(i,end=' ')
#=================================================================
# a=int(input())

# for i in range(a):
#     for j in range(a-i-1,0,-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("*", end="")
#     print()

# for i in range(a-1):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(2*(a-i-1)-1):
#         print("*", end="")
#     print()
#=================================================================
# n=list(input())
# sum1=1

# for i in range(len(n)//2):
#     if n[i]!=n[-(i+1)]:
#         sum1=0
#         break
# print(sum1)

# num=[]
# for i in range(10):
#     row=list(map(int, input().split()))
#     num.append(row)

# Fwone = [[0 for _ in range(10)] for _ in range(10)]

# re=0
# def island(num1, num2):
#     if num1 < 0 or num1 >= 9 or num2 < 0 or num2 >= 10 or Fwone[num1][num2] == 1 or num[num1][num2] == 0:
#         return
#     Fwone[num1][num2] = 1

#     island(num1 + 1, num2) 

#     island(num1 , num2+ 1) 

#     island(num1 - 1, num2)

#     island(num1, num2 - 1)


# for i in range(4):
#     for j in range(5):
#         if num[i][j] == 1 and Fwone[i][j] == 0:
#             island(i, j)
#             re+=1

# print(f"number of islands : {re}")
