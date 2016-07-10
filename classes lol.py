import re
class Node(object):
    def __init__(self):
        self.item = None
        self.link = None

class Stack(object):
    def __init__(self):
        self.top = 0
        self.head = Node()
    def isEmpty(self):
        return self.top == 0
    def push(self, item):
        oldHead = self.head
        self.head = Node()
        self.head.item = item
        self.head.link = oldHead
        self.top += 1
    def pop(self):
        item = self.head.item
        self.head = self.head.link
        self.top -= 1
        return item

class kurwa(object):
    def __init__(self, nya):
        self.nya = str(nya)
        self.l = re.split("([^0-9])", self.nya)
        self.stack = Stack()
    def calc(self):
        for t in self.l:
            if t == '' or t == ' ':
                continue
            elif t == '+':
                sum = self.stack.pop() + self.stack.pop()
                self.stack.push(sum)
            elif t == '-':
                diff = -(self.stack.pop() - self.stack.pop())
                self.stack.push(diff)
            elif t == '*':
                prod = self.stack.pop() * self.stack.pop()
                self.stack.push(prod)
            elif t == '/':
                division = 1/(self.stack.pop() / self.stack.pop())
                self.stack.push(division)
            else:
                self.stack.push(int(t))
        return self.stack.pop()
    def __str__(self):
        return 'input : ' +str(self.nya)+ ' ' + 'output : ' + str(self.calc())
a = kurwa('8 2 5*+ 1 3 2*+ 4 -/')
# print(a.l)
print(a.calc())
print(a)
