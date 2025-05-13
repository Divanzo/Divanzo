class Studnt:
    def __init__(self,name,grade,Class): #생성자,초기화
        self.name=name
        self.grade=grade
        self.Class=Class
    def introduce(self):
        print(f"안녕 나는 {self.grade}학년 {self.Class}반 {self.name}이야")

s1=Studnt('수민',1,3)
s2=Studnt('건우',3,1)

s1.introduce()
s2.introduce()