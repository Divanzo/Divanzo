print("#"*25)
print("분초 계산 프로그램")
print("#"*25)

s=int(input("초 입력: "))
m=s//60
s%=60

if m>=60:
    h=m//60
    m%=60

print(f"결과: {h}시간 {m}분 {s}초")
