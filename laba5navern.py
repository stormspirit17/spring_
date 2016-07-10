class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def find(self, data):
        if self.value == data:
            return True
        if self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    def inorder(self):
        # import pdb; pdb.set_trace()
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()
        return 'Done'


class Tree(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def inorder(self):
        print('INORDER')
        return self.root.inorder()

bst = Tree()
a = [8, 4, 7, 3]
for elem in a:
    bst.insert(elem)
print(bst.inorder())
