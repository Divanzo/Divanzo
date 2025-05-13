while True:
    try:
        score_list=[]
        score_list=list(map(int,input().split()))

        sum1=sum(score_list)
        avg=sum1/2
    except ValueError:
        print('잘못된 입력입니다. 종료.')
        break
    else:    
        print(f'합계:{sum1}, 평균:{avg}')
