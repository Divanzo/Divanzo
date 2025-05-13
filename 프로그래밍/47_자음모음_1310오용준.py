word=input("영문자열 입력: ")
con=0
vow=0
eng=0
num=0
space=0
#Welcome to korea
print()
print('#'*25)

for i in word:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        con+=1
    elif i==i.isalpha():
        eng+=1
    elif i==i.isdigit():
        num+=1
    elif i==i.isspace():
        space+=1
    else:
        if i!=' ':
            vow+=1
    
print()

print('모음 개수:',con,end=' ')
print('자음 개수:',vow)
print('영문자 개수:',eng)
print('숫자 개수:',num)