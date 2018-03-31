# Get Path to a NoDE

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

    def pathToNode(self, target: BTNode):
        if self.root is None:
            return []
        return self._pathToNodeRec(self.root, target, [self.root])

    def _pathToNodeRec(self, root, target, path: list):
        if root == target:
            print(path)
            return path
        if root.left:
            resLeft = self._pathToNodeRec(root.left, target, path + [root.left])
            if resLeft:
                return resLeft
        if root.right:
            resRight = self._pathToNodeRec(root.right, target, path + [root.right])
            if resRight:
                return resRight
```