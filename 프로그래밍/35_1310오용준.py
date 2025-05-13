hap=0
avg=0

num_list=[]

while True:
    s=float(input("점수: "))

    if s<0:
        print(f"합계: {hap}",end=" ")
        print(f"평균: {avg:.1f}")
        break

    else:
        num_list.append(s)
        
        hap+=s
        avg=hap/len(num_list)