birth,information=map(int, input().split(','))

present=2025

birth=birth//10000

if information==1 or information==3:
    
    if information==1:
        result=(present+1)-(1900+birth)
        gen="남성"
    
    else:
        result=(present+1)-(2000+birth)
        gen="남성"

if information==2 or information==4:
    
    if information==2:
        result=(present+1)-(1900+birth)
        gen="여성"
    
    else:
        result=(present+1)-(2000+birth)
        gen="여성"

print(f"현재나이 {result}살 {gen}입니다.")