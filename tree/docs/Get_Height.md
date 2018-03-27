# Get Height of a Binary Tree

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

    def maxDepth(self):
        return self._maxDepthRec(self.root)

    def _maxDepthRec(self, root: BTNode):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None and root.right is not None:
            return 1 + self._maxDepthRec(root.right)
        elif root.left is not None and root.right is None:
            return 1 + self._maxDepthRec(root.left)
        else:
            return 1 + max(self._maxDepthRec(root.left),
                           self._maxDepthRec(root.right))
           
    def minDepth(self):
        return self._minDepthRec(self.root)

    def _minDepthRec(self, root):
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return 1
        else:
            return 1 + min(self._minDepthRec(root.left),
                           self._minDepthRec(root.right))

    def isBalance(self):
        if self.maxDepth() - self.minDepth() <= 1:
            return True
        return False
```