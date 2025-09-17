class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = 0

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity-1

    def push(self, item):
        if not self.is_full():
            self.array[self.top] = item
            self.top += 1
        else:
            print("Stack overflow")
    
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top-1]
            self.top -= 1
            return item
        else:
            print("Stack underflow")
    
    def peek(self):
        if not self.is_empty():
            return self.array[self.top-1]
        else: pass

    def __str__(self):
        return str(self.array[0:self.top+1][::-1])

    def size(self):
        return self.top+1

if __name__ == "__main__":
    
