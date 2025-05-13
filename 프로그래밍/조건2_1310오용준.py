# b=int(input("score"))

# if b==100:
#     print("pass")

# else:
#     print("Not enough")

# li=list(input())

# repeatnum=len(li)

# input_num=int(input("Enter a number: "))

# for i in range(input_num):
    
#     arrow=input()

#     if "P" in arrow:
#         li.insert(repeatnum,arrow[-1])
#         repeatnum+=1

#     elif "L" in arrow:
#         if repeatnum!=0:
#             repeatnum-=1

#     elif "D" in arrow:
#         if repeatnum!=len(li):
#             repeatnum+=1

#     elif "B" in arrow:
#         if repeatnum!=0:
#             li.pop(repeatnum-1)
#             repeatnum-=1

# for row in li:
#     print(row,end="")

#디렉터
# a=list(input())
# left=a
# right=[]

# n=int(input())

# for i in range(n):
#     a=input()
#     if "L" in a:
#         if left:
#             right.append(left.pop())
#     elif "D" in a:
#         if right:
#             left.append(right.pop())
#     elif "B" in a:
#         if left:
#             left.pop()
#     elif "P" in a:
#         left.append(a.split(" ")[1])

# for i in left:
#     print(i,end="")
# for i in range(len(right)-1,-1,-1):
#     print(right[i],end="")

# _open1="("
# _close1=")"
# _open2="["
# _close2="]"
# stack1=[]
# stack2=[]
# result="YES"  
    
# a=input()

# for i in a:
#     if i==_open1:
#         stack1.append(i)
#     elif i==_open2:
#         stack2.append(i)
#     elif i==_close1:
#         if len(stack1)==0:
#             result="NO"
#         else:
#             stack1.pop()
#     elif i==_close2:
#         if len(stack2)==0:
#             result="NO"
#             break
#         else:
#             stack2.pop()
# if len(stack1)!=0 or len(stack2)!=0:
#     result="NO"
# print(result)

#==============================================
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

#=============================================================
n=int(input())

colorway=[]

normals_colorway=[list(input()) for _ in range(n)]
bitchs_colorway=normals_colorway

normal_Checklist=[[0 for _ in range(n)] for _ in range(n)]
bitch_Checklist=[[0 for _ in range(n)] for _ in range(n)]

normal=0
bitch=0

def main(x,y,cr):
    if x<0 or x>len(normals_colorway)-1 or y>len(normals_colorway[0])-1 or y<0 or normal_Checklist[x][y]==1 or normals_colorway[x][y]!=cr:
        return
    normal_Checklist[x][y]=1

    main(x-1,y,cr)
    main(x+1,y,cr)
    main(x,y-1,cr)
    main(x,y+1,cr)

def main_2(x2,y2,cr2):
    if x2<0 or x2>len(bitchs_colorway)-1 or y2>len(bitchs_colorway[0])-1 or y2<0 or bitch_Checklist[x2][y2]==1 or bitchs_colorway[x2][y2]!=cr2:
        return
    bitch_Checklist[x2][y2]=2

    main_2(x2-1,y2,cr2)
    main_2(x2+1,y2,cr2)
    main_2(x2,y2-1,cr2)
    main_2(x2,y2+1,cr2)

for i in range(len(normals_colorway)):
    for j in range(len(normals_colorway)):
        if normal_Checklist[i][j]==0:
            normal+=1
            main(i,j,normals_colorway[i][j])

for i in range(len(bitchs_colorway)):
    for j in range(len(bitchs_colorway)):
        if bitchs_colorway[i][j]=='G':
            bitchs_colorway[i][j]=='R'

        if bitch_Checklist[i][j]==0:
            bitch+=1
            main_2(i,j,bitchs_colorway[i][j])

print(f'{normal} {bitch}')





