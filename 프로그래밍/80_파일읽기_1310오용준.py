f=open('data_2.txt','r')

lines=f.readlines()
print(lines)

for line in lines:
    # line=line.strip() or line.rstrip() or line.lstrip()
    print(line.strip())

f.close()