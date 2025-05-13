a,b,c=map(int, input("세 수를 입력하시오:").split())

sum1=0

if (a>b and a<c) or (a<b and a>c): #a중심
    sum1+=a

elif (b>a and b<c) or (b>a and b<c): #b중심
    sum1+=b

elif (c<a and c>b) or (c>a and c<b): #c중심
    sum1+=c

print(f"두번째 수는 {sum1}입니다.")
