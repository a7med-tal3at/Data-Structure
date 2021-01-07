class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        return not self.head

    def append(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def appendFirst(self, val):
        if self.isEmpty():
            self.append(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def appendAtPos(self, pos, val):
        if pos == self.tail.val:
            self.append(val)
        elif pos == self.head.val:
            self.appendFirst(val)
        else:
            tmp = self.head
            while tmp != None:
                if tmp.next.val == pos:
                    tmp2 = tmp.next
                    newNode = Node(val)
                    tmp.next = newNode
                    newNode.prev = tmp
                    newNode.next = tmp2
                    tmp2.prev = newNode
                    break
                tmp = tmp.next
                
    def delete(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def deleteFirst(self):
        self.head = self.head.next
        self.head.prev = None

    def deleteAtPos(self, pos):
        if pos == self.tail.val:
            self.delete()
        elif pos == self.head.val:
            self.deleteFirst()
        else:
            tmp = self.head
            while tmp != None:
                if tmp.next.val == pos:
                    tmp2 = tmp.next 
                    tmp.next = tmp2.next
                    tmp2.next.prev = tmp
                    break
                tmp = tmp.next

    def display(self):
        if self.isEmpty():
            print("Can't Display")
            return

        tmp = self.head
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next

if __name__ == "__main__":
    dll = doublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.deleteAtPos(20)
    dll.appendAtPos(30, 20)
    dll.appendFirst(-1000)
    dll.display()