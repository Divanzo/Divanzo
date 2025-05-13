f=open("data_1.txt","w")
f.write("안녕하세요\n")

content=input()
f.write(f"{content}\n")

f.close()