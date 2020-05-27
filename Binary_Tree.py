class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.right = None
            self.root.left = None
        else:

            if data < self.root.data:
                if self.root.left is None:
                    self.root.left = Node(data)
                else:
                    self.root.left.insert(data)
            else:
                if self.root.right is None:
                    self.root.right = Node(data)
                else:
                    self.root.right.insert(data)
