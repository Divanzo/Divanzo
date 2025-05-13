#51-1
def fun_s(a):
    sum1=0
    
    for i in range(1,a+1):
        sum1+=i
    
    return sum1

print(fun_s(10))
print(fun_s(100))
print(fun_s(1000))

#=========================================
#51-2-1
# def fun_fact(k):
#     sum1=1

#     for i in range(1,k+1):
#         sum1*=i
    
#     return sum1
# print(fun_fact(5))

#51-2-2
def fun_fact(k):
    
    if k==1:
        return 1
    else:
        return k*fun_fact(k-1)

print(fun_fact(5))
#============================================