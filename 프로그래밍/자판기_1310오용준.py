change=0
n=0
while n<5:
    money=int(input("돈을 넣어주세요: "))
    # money=change+money
    juice=800

    if money<juice:
        print("**금액이 부족하오.")
        print(f"**돈을 넣어주세요.")
        n-=1
        
    if n==4:
        print("주스가 매진되었습니다.")

    else:
        change=money-juice
        print(f"맛있는 주스 드시고 잔돈{change}원 받으세요.")
    n+=1