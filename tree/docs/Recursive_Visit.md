# Binary Tree Recursively Visit

```python
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
```