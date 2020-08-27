'''
Deque

addFront(element): Add element to the front of the Deque
addBack(element): Add element to the back of the Deque
peekFront(): Look at the element at the front of the Deque
peekBack(): Look at the element at the back of the Deque
removeFront(): Remove the element at the front of the Deque
removeBack(): Remove the element at the back of the Deque
'''

class Deque:
    def __init__(self):
        self.value = []

    def addFront(self, element):
        if len(self.value) > 0 :
            self.value.insert(0,element)
        else :
            self.addBack(element)

    def addBack(self, element) :
        self.value.append(element)

    def peekFront(self) : 
        if len(self.value) > 0 :
            return self.value[0]
        else :
            return False

    def peekBack(self): 
        return self.value[len(self.value)-1] if len(self.value) > 0 else False

    def removeBack(self): 
        if len(self.value) > 0:
            del self.value[len(self.value)-1]

    def removeFront(self): 
        if len(self.value) > 0:
            del self.value[0]

    def showData(self):
        print(self.value)


deque = Deque()
print("Deque")
deque.addBack(5)
deque.addFront(1)
print(deque.peekFront())
deque.addFront(3)
deque.addFront(8)
print(deque.peekBack())
deque.addFront(15)
deque.removeBack()
deque.showData()
deque.addFront(11)
print(deque.peekBack())
deque.addFront(13)
deque.addBack(11)
deque.addBack(20)
deque.removeFront()
deque.showData()
deque.addFront(81)
deque.addBack(31)
deque.showData()

class Queue:
    def __init__(self):
        self.deque = Deque()
    def enqueue(self, element):
        return self.deque.addBack(element)
    def peek(self):
        return self.deque.peekFront()
    def dequeue(self):
        self.deque.removeFront()
    def showData(self):
        self.deque.showData()
    def __len__(self):
        return len(self.deque)


queue = Queue()
print("Queue")
queue.enqueue(5) # [5]
queue.enqueue(1) # [5,1]
print(queue.peek()) # [5,1]
queue.enqueue(3) # [5,1,3]
queue.enqueue(8) # [5,1,3,8]
print(queue.peek()) # [5,1,3,8]
queue.enqueue(15) # [5,1,3,8,15]
queue.dequeue() # [1,3,8,15]
queue.showData() # [1,3,8,15]
queue.enqueue(11) # [1,3,8,15,11]
print(queue.peek()) # [1,3,8,15,11]
queue.enqueue(13) # [1,3,8,15,11,13]
queue.enqueue(11) # [1,3,8,15,11,13,11]
queue.enqueue(20) # [1,3,8,15,11,13,11,20]
queue.dequeue() # [3,8,15,11,13,11,20]
queue.showData() # [3,8,15,11,13,11,20]
queue.enqueue(81) # [3,8,15,11,13,11,20,81]
queue.enqueue(31) # [3,8,15,11,13,11,20,81,31]
queue.showData() # [3,8,15,11,13,11,20,81,31]


class Stack:
    def __init__(self):
        self.deque = Deque()
    def push(self, element):
        return self.deque.addBack(element)
    def top(self):
        return self.deque.peekBack()
    def pop(self):
        self.deque.removeBack()
    def showData(self):
        self.deque.showData()
    def __len__(self):
        return len(self.deque)

stack = Stack()

print("Stack")
stack.push(1)
stack.push(4)
stack.push(7)
stack.showData()
stack.pop()
stack.showData()
print(stack.top())
stack.showData()
stack.push(8)
stack.push(18)
stack.push(1)
stack.showData()

s = Stack()
for i in range(10):
    s.push(i)
s.pop()
s.push(100)
s.push(200)
s.pop()
s.pop()
s.pop()
s.showData()
print(s.top())