# while True:
id=input("id를 입력하시오: ")

if id=='dgsw':
    pw=input("비밀번호를 입력하시오: ")
        
    if pw=='high':
        print("로그인 성공")
        # break
    else:
        print('로그인실패: 비밀번호 불일치')
    
else: 
    print("비밀번호 불일치: 아이디 불일치")

