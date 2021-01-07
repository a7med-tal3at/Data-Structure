class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
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
            self.tail = self.tail.next


    def appendFirst(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.append(val)
        else:
            newNode.next = self.head
            self.head = newNode


    def appendPos(self, pos, val):
        newNode = Node(val)
        tmp = self.head
        if self.isEmpty() or pos == self.head.val:
            self.appendFirst(val)
        elif pos == self.tail.val:
            self.append(val)
            print('insert a valid values')
            return
        else:
            while tmp != None:
                if tmp.next.val == pos:
                    tmp2 = tmp.next
                    tmp.next = newNode
                    newNode.next = tmp2
                    tmp2 = None
                    break
                tmp = tmp.next
                

    def delete(self):
        if self.isEmpty():
            print('Can\'t delete')
            return
        tmp = self.head
        while tmp != None:
            if tmp.next == self.tail: 
                self.tail = tmp
                self.tail.next = None
                tmp = None
                break
            tmp = tmp.next
        

    def deleteFirst(self):
        if self.isEmpty():
            print('Can\'t delete')
            return
        self.head = self.head.next

    def deleteMid(self, pos):
        tmp = self.head
        if self.isEmpty() or pos == self.head.val:
            self.deleteFirst()
        elif pos == self.tail.val:
            self.delete()
            print('insert a valid values')
            return
        else:
            while tmp != None:
                if tmp.next.val == pos:
                    tmp2 = tmp.next.next
                    tmp.next = tmp2
                    tmp2 = None
                    break
                tmp = tmp.next

    def display(self):
        tmp = self.head
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.appendPos(20, 15)
    ll.appendPos(20, 150)
    ll.deleteMid(150)
    ll.deleteMid(15)
    ll.display()


