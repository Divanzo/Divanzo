height=int(input("키(cm) 입력:"))
weight=int(input("몸무게(kg) 입력:"))

print('*'*25)

if 130<=height<190 and 25<=weight<100:
    print('이용 가능')

else:
    print('이용 불가능')