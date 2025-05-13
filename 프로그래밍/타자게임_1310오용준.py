#타자게임
import time
import random

w=['cat','bat','rat','mat','sat','pat','fat','hat','nat','vat']
n=0

start=time.time()

print('시작!')

while True:
    random.shuffle(w)
    q=random.choice(w)
    print(q)

    word=input("타자 연습: ")
    
    if word==q:
        print('pass')
        n+=1
        print()
        continue

    elif word=='0':
        print('끝!')

        end=time.time()

        print(f'걸린시간:{end-start}')
        print(f'맞은 횟수:{n}')
        print()
        break

    elif q!=word and word!='0':
        print('땡!')
        print()
        continue
