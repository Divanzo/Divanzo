f=open('data_2.txt','a')

for i in range(11,21):
    line=f"{i}번째 줄입니다."
    f.write(f"{line}\n")
f.close()