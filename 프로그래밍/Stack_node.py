class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

class LinkedList:
    def __init__(self):
        self.head = None

def isEmpty(self):
    return self.head is None

def isFull(self):
    return False

def getNode(self, pos):
    if pos<0:
        return None
    node = self.head

    while pos>0 and node is not None:
        node = node.link
        pos -= 1

    return node

def getEntry(self, pos):
    node = getNode(pos)
    if node is None:
        return None
    else:
        return node.data

def insertNode(self, pos, elem):
    before = getNode(pos-1)
    if before is None:
        node = Node(elem, self.head)
    else:
        before.link = none

def delete(self, pos):
    before = getNode(pos-1)
    if before is None:
        if self.head is not None:
            self.head = self.head.link
    else:
        before.link = before.link.link

def __str__(self):
    arr = []
    node = self.head
    while node is not None:
        arr.append(node.data)
        node = node.link
    return str(arr)

if __name__ == "__main__":
    L = LinkedList()
    print(L)
    L.insertNode(0, 10)
    print(L)
    L.insertNode(0, 20)
    print(L)
    L.insertNode(1, 30)
    print(L)
    L.insertNode(3, 40)
    print(L)
    L.insertNode(2, 50)
    print(L)
    L.delete(2)
    print(L)
    L.delete(3)
    print(L)
    L.delete(0)
    print(L)
    print(f"20의 위치: {L.findNode(20)}")