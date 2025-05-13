grade=int(input("과일 무게(g):"))

if 210<=grade<375:
    if 300<=grade<375:
        print('특')
    elif 250<=grade<300:
        print('상')
    else:
        print('보통')

else:
    print('판정 불가')
