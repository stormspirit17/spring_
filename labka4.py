class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def addLast(self, e):
        node = Node(e)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addFirst(self, e):
        node = Node(e)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def add(self, index, e):
        if index < 0 or index > self.length:
            return
        if self.length == 0:
            self.addLast(e)
            return
        if index == 0:
            self.addFirst(e)
            return
        if index == self.length:
            self.addLast(e)
            return
        node = self.head
        i = 0
        while i < index-1:
            node = node.next
            i += 1
        newNode = Node(e, node.next)
        node.next = newNode

    def takefirst(self):
        if self.length == 0:
            raise IndexError('Your list is empty')
        else:
            node = self.head
            self.head = node.next
            self.length -= 1
        return node

    def takelast(self):
        prev = None
        node = self.head
        i = 0
        while node is not None and i < self.length-1:
            prev = node
            node = node.next
            i += 1
        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next
        self.length -= 1
        return node

    def remove(self, index):
        prev = None
        node = self.head
        i = 0
        while node is not None and i < index:
            prev = node
            node = node.next
            i += 1
        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next
        self.length -= 1
        return node
    def set(self, index, e):
        self.remove(index)
        self.add(index, e)
    def get(self, index):
        node = self.head
        i = 0
        while node is not None and i < index:
            node = node.next
            i += 1
        return node

    def insertionSortList(self):
        head = self.head
        a = self.length
        if head == None:
            return None
        pseudoHead = Node(-1)

        pseudoHead.next = head
        current = head.next
        head.next = None
        sortedEnd = head
        while current is not None:
            nextCurrent = current.next
            if sortedEnd.cargo <= current.cargo:
                sortedEnd.next = current
                current.next = None

                sortedEnd = current
            else:
                headOfSorted = pseudoHead
                while headOfSorted.next.cargo < current.cargo:
                    headOfSorted = headOfSorted.next

                current.next = headOfSorted.next
                headOfSorted.next = current

            current = nextCurrent
        i=0
        self.length = 0
        while i < a:
            pseudoHead = pseudoHead.next
            self.addLast(pseudoHead)
            i += 1
        return self

    def __str__(self):
        node = self.head
        string = ''
        while node:
            string += str(node) + ' '
            node = node.next
        return string

l = LinkedList()
l.addLast('g')
l.addLast('a')
l.addLast('z')
print(l)
l.remove(0)
print(l)
l.addLast(300)
l.addFirst('meow')
print(l)
l.takefirst()
print(l)
l.addLast(400)
l.takelast()
print(l)
print(l.get(1))
l.set(0, 'KPI')
print(l)
m = LinkedList()
m.addLast(300)
m.addLast(-31)
m.addLast(123)
m.addLast(0)
print(m)
m.insertionSortList()
print(m)