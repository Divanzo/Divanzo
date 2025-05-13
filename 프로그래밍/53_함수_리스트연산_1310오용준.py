def lst_create():
    data=list(map(float, input().split()))
    return data

def lst_append(data):
    while True:
        try:
            a=float(input())
            
        except ValueError:
            break
        
        else:
            data.append(a)
    return tuple(data)

def lst_cal(lst_ff):
    sum1=0
    sum(lst_ff)
    
    return sum1/len(lst_ff)

def lst_print(R1,R2):
    print(R1,R2)

lst_s=lst_create()

lst_f=lst_append(lst_s)

result=lst_cal(lst_f)

lst_print(lst_f,result)