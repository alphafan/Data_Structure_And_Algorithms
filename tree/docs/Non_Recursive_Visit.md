# Binary Tree Non Recursive Visit

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
        
    def inOrder(self):
        print('In-Order    :', end=' ')
        if self.root is None:
            print()
            return
        node = self.root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                print(node, end=' ')
                node = node.right
        print()

    def postOrder(self):
        print('Post-Order  :', end=' ')
        stack = [self.root]
        prev = None
        while stack:
            curr = stack[-1]
            # 3 conditions to print out
            if (curr.left is None and curr.right is None) or \
               (prev is not None and curr.left == prev and curr.right is None) or \
               (prev is not None and curr.right == prev):
                node = stack.pop()
                print(node, end=' ')
                prev = node
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        print()
```