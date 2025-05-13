class Counter:
    def __init__(self):
        self.counter=0
    
    def reset(self,initValue=0):
        self.counter=initValue
    
    def incrementself(self):
        self.counter+=1
    
    def get(self):
        return f'{self.counter}'
    
a=Counter()

a.reset(0)
a.incrementself()
print(a.get())

b=Counter()

b.reset(100)
b.incrementself()
print(b.get())
