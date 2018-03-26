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
```