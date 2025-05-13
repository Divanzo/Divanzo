# ver1
f=open('me.txt','w')

name=input('이름: ')
age=int(input('나이: '))
school=input('학교: ')

f.write(f"이름:{name}\n")
f.write(f"나이:{age}\n")
f.write(f"학교:{school}\n")
f.close()
print("정상 종료")

# ver2
name=input('이름: ')
age=int(input('나이: '))
school=input('학교: ')

with open('me.txt','w') as f:
    f.write(f"이름:{name}\n")
    f.write(f"나이:{age}\n")
    f.write(f"학교:{school}\n")
print("정상 종료")