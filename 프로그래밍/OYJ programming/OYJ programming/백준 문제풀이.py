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

#=================================================================
# word=list(input())

# clone1=word.copy()
# clone2=word.copy()

# clone1.sort()
# alist = clone1

# clone2.sort(reverse=True)
# blist = clone2

# sum1='0'
# sum2='0'
# for i in alist:
#     sum1+=i
# for i in blist:
#     sum2+=i

# sum1 = sum1.lstrip('0')
# sum2 = sum2.lstrip('0')

# sum1 = int(sum1)
# sum2 = int(sum2)

# print(sum2-sum1)
#=================================================================

# name=list(input().split())

# votes=list(input().split())
# result=[]

# for i in name:
#     sum1=0
#     for j in votes:
#         if i==j:
#             sum1+=1
#     solution={i:sum1}
#     result.append(solution)

# final_result = {}
# for r in result:
#     final_result.update(r)

# sorted_result = sorted(final_result.items(), key=lambda x: x[1], reverse=True)

# print(sorted_result[0][0],sorted_result[1][0])

# Latte Americano Espresso
# Latte Americano Espresso Latte Americano Americano Latte Latte Latte

#=================================================================

# n=int(input('정수를 입력하세요: '))
# numlist=list(map(int, input().split()))
# result=[]

# for i in range(len(numlist)):
#     for j in range(len(numlist)):
#         if n-numlist[i]>n-numlist[j]:
#             numlist[i], numlist[j] = numlist[j], numlist[i]
#         elif n-numlist[i]==0:
#             numlist.insert(0,numlist[i])
#         else:
#             numlist.append(numlist[i])

# print(numlist)

#==================================================================

#웜 바이러스
# n,m= map(int, input().split())
# # n: 컴퓨터의 수, m: 연결된 컴퓨터 쌍의 수

# # 그래프 초기화 (1번부터 시작하므로 n+1)
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)

# # 연결 정보 저장
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 큐 구현 (리스트로 직접)
# queue = [1]
# visited[1] = True
# count = 0

# # BFS 시작
# while queue:
#     current = queue[0]
#     del queue[0]  # pop(0) 대신
#     for neighbor in graph[current]:
#         if not visited[neighbor]:
#             visited[neighbor] = True
#             queue.append(neighbor)
#             count += 1

# print(count)


#DFS
import sys
#재귀 깊이 제한 뚫기
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

graph = [[] for _ in range(a)]
visited = [False] * a

# 인접 리스트 구성 (0-indexed)
for _ in range(b):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)3
    graph[y-1].append(x-1)

def dfs(graph, start, visited):
    visited[start] = True
    count = 0
    for i in graph[start]:
        if visited[i]==False:
            count += 1  # 감염 수 증가
            count += dfs(graph, i, visited)  # 재귀로 더 깊이 감염 탐색
    return count

result = dfs(graph, 0, visited)
print(result)