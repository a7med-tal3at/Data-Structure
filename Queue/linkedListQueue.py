class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return not self.front

    def enQueue(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = self.rear.next

    def deQueue(self):
        if self.isEmpty():
            print("Can't deQueue")
            return
            
        value = self.front.val
        self.front = self.front.next
        return value

    def display(self):
        if self.isEmpty():
            print("Can't deQueue")
            return
        while True:
            if self.isEmpty():
                break
            print(self.deQueue())

if __name__ == "__main__":
    q = Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(15)
    q.enQueue(20)
    q.deQueue()
    q.display()