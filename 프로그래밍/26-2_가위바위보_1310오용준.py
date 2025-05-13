import random as r

game_list=['가위','바위','보']

user=int(input("입력(1.가위 2.바위 3.보): "))
com_list=r.choice(game_list)

print(f"User: {game_list[user-1]} Com: {com_list} ->",end=" ")

#인덱스 값으로 변환후 비교#|
User_ans=game_list.index(game_list[user-1])

Com_ans=game_list.index(com_list)
#####################|

if User_ans>Com_ans:
    print("승리")
elif User_ans==Com_ans:
    print("draw")
else:
    print("패배")