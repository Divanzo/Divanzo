import random as r

def genPass():
    chrs='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password=''
    for i in range(8):
        password += r.choice(chrs)
    return password

for i in range(3):
    result=genPass()
    print(f"암호{i+1}: \033[31m {result} \033[0m")