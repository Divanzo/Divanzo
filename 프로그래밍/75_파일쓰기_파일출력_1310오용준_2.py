f=open('data_3.txt','w')

while True:
    content=input()

    if content!="":
        f.write(f"{content}\n")
    else:
        break
f.close()
print("정상 종료")