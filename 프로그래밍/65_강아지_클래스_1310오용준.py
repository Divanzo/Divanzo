class Dog: #Dog: 클래스명
    def __init__(self, name, age, kind): #name, age, kind = 속성
        self.name=name
        self.age=age
        self.kind=kind

    def bark(self): #메소드1: 짖기
        print(f'{self.name}가 멍멍 짖어요.')

    def sit(self): #메소드2: 앉기
        print(f'{self.kind}은 앉기도 잘해요.')        

my_dog=Dog("망고",3,"푸들")
my_dog.bark()

my_dog=Dog("호야",5,"진도")
my_dog.sit()


class Cat:
    species='고양이'
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def introduce(self):
        print(f'안녕 난 {self.color}색 {Cat.species} {self.name}야') #(Cat.변수)는 인자를 바로 가져오기.

my_cat=Cat("벌이",'연한치즈')
my_cat.introduce()