# Binary Tree Level Order Visit

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

    def levelOrder(self):
        """ Visit Tree Level by Level """
        print('Level Order :', end=' ')
        if self.root is None:
            print()
            return
        currLevel = [self.root]
        nextLevel = []
        while currLevel or nextLevel:
            while len(currLevel) != 0:
                node = currLevel.pop(0)
                print(node, end=' ')
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel, nextLevel = nextLevel, currLevel
        print()
```