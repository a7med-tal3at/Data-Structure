class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        
        return not self.top

    def push(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.isEmpty():
            print("The Stack Is Empty")
            return
        rtl = self.top.val
        self.top = self.top.next
        return rtl

    def display(self):

        while True:
            if self.isEmpty():
                break
            print(self.pop())
        

if __name__ == "__main__":
    s = Stack()   
    s.push(5)
    s.push(10)
    s.display()



