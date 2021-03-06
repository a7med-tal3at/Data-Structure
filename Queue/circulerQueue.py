class Queue:
    def __init__(self, size):
        self.size = size
        self.front = self.rear = self.len = 0
        self.arr = [None] * self.size

    def isFull(self):
        return self.len == self.size

    def isEmpty(self):
        return self.len == 0

    def enQueue(self, val):
        if self.isFull():
            print('Can\'t enQueue')
            return
        
        self.arr[self.rear] = val
        self.rear = (self.rear +1) % self.size
        self.len +=1
    
    def deQueue(self):
        if self.isEmpty():
            print('Can\'t deQueue')
            return

        self.front = (self.front +1) % self.size
        self.len-=1
    
    def display(self):
        if self.isEmpty():
            print('Can\'t deQueue')
            return

        for i in range(self.front, self.size):
            print(self.arr[i])


if __name__ == "__main__":
    q = Queue(5)
    q.enQueue(1)
    q.enQueue(10)
    q.enQueue(100)
    q.enQueue(1000)
    q.enQueue(10000)
    q.deQueue()
    q.display()