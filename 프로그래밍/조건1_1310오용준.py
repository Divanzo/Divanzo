# a=int(input("score: "))

# if a<10:
#     print("small than 10")

# print("END")


M,N,K=map(int,input().split())

alist=[[0 for _ in range(N)] for _ in range(M)]
store=[]

for i in range(K):
    x1,y1,x2,y2=map(int,input().split())

    for j in range(y1,y2):
        for k in range(x1,x2):
            alist[j][k]=1

for row in alist:
    print(row)

cnt=0
for i in range(M):
    for j in range(N):
        
        if alist[i][j]==0:
            cnt+=1

print(cnt)