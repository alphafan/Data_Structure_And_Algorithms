class TNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class AVLTree(object):

    def __init__(self):
        pass

    def insert(self, root, value):
        if root is None:
            return TNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        if value > root.value:
            root.right = self.insert(root.right, value)
        root = self.reBalance(root)
        return root

    def reBalance(self, root):
        if root is None:
            return
        while self.height(root.left) - self.height(root.right) > 1:
            root = self.rotateRight(root)
        while self.height(root.right) - self.height(root.left) > 1:
            root = self.rotateLeft(root)
        return root

    def height(self, root):
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.height(root.right)
        if root.right is None:
            return 1 + self.height(root.left)
        return 1 + max(self.height(root.left), self.height(root.right))

    def rotateLeft(self, root):
        if root is None or root.right is None:
            return root
        right = root.right
        root.right = right.left
        right.left = root
        return right

    def rotateRight(self, root):
        if root is None or root.right is None:
            return root
        left = root.left
        root.left = left.right
        left.right = root
        return left


root = TNode(0)
tree = AVLTree()
for i in range(1, 7):
    root = tree.insert(root, i)
print(root.value)
print(root.left.value, root.right.value)
print(root.left.left.value, root.left.right.value, root.right.left.value, root.right.right.value)
