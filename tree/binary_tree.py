# A simple implementation of binary tree


class BTNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


class BTree(object):

    def __init__(self, root):
        self.root = root

    def preOrderRec(self):
        print('Pre-Order Rec: ', end=' ')
        self._preOrderRec(self.root)
        print()     # Flush

    def _preOrderRec(self, root: BTNode):
        if root:
            print(root.value, end=' ')
            self._preOrderRec(root.left)
            self._preOrderRec(root.right)

    def inOrderRec(self):
        print('In-Order Rec:  ', end=' ')
        self._inOrderRec(self.root)
        print()     # Flush

    def _inOrderRec(self, root: BTNode):
        if root:
            self._inOrderRec(root.left)
            print(root.value, end=' ')
            self._inOrderRec(root.right)

    def postOrderRec(self):
        print('Post-Order Rec:', end=' ')
        self._postOrderRec(self.root)
        print()  # Flush

    def _postOrderRec(self, root: BTNode):
        if root:
            self._postOrderRec(root.left)
            self._postOrderRec(root.right)
            print(root.value, end=' ')

    def preOrder(self):
        print('Pre-Order:   ')
        if self.root is None:
            print()
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node, end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print()


def buildTree():
    """  Build a tree for testing

    Tree Structure:
            a
          /   \
         b     c
       /  \   / \
      d   e  f   g
    """
    a, b, c, d, e, f, g = (BTNode(i) for i in 'abcdefg')
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    return BTree(root=a)


tree = buildTree()
tree.preOrderRec()
tree.inOrderRec()
tree.postOrderRec()
tree.preOrder()