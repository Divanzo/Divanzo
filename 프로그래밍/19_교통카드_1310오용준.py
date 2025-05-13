# fee=850
# card=int(input("카드잔액: "))

# if card>=fee:
#     print("학생입니다.")

# else:
#     print("얼굴이 학생이 맞나요?")

fee=850
card=int(input("카드잔액: "))

if card>=fee:
    print("pass")

elif card<fee:
    print("fail")