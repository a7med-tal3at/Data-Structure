# Simple Stack Using Array 
# implementation in python3
class Stack:
    def __init__(self, size):
        self.top = -1 
        self.size = size
        self.arr = [None] * self.size

    def isEmptyVald(func):
        def nestFunc(self):
            if self.top == -1:
                print('The Stack is Empty')
            else:
                func(self)

        return nestFunc

    def push(self, val):
        self.top += 1
        if self.top == self.size:
            print("The Stack Is Full")
            return
        self.arr[self.top] = val
    
    @isEmptyVald
    def pop(self):
        self.top -= 1

    @isEmptyVald
    def display(self):
        for i in range(self.top, -1, -1):
            print(self.arr[i])
            

if __name__ == '__main__':
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.display()