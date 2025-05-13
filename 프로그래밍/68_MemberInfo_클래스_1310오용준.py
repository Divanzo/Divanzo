class Info:
    def __init__(self,idx,password,name):
        self.idx=idx
        self.password=password
        self.name=name
    
    def getmember(self):
        return f'{self.idx},{self.password},{self.name}'


my_member=Info('king','12345','홍길동')

print(my_member.getmember())