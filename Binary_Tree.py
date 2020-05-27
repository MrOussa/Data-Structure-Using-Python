class Node:
    # declaration of The Node tree
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

        else:
            self.data = data

    def printTree(self):
        if self.left is not None:
            self.left.printTree()
        print(self.data)
        if self.right is not None:
            self.right.printTree()

    def InOrder_Traverse(self, root):
        # left --- root --- right
        res = []
        if root:
            res = self.InOrder_Traverse(root.left)
            res.append(root.data)
            res = res + self.InOrder_Traverse(root.right)
        return res

    def PreOrder_Traverse(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrder_Traverse(root.left)
            res = res + self.PreOrder_Traverse(root.right)
        return res

    def PostOrder_Traverse(self, root):
        res = []
        if root:
            res = res + self.PreOrder_Traverse(root.left)
            res = res + self.PreOrder_Traverse(root.right)
            res.append(root.data)
        return res