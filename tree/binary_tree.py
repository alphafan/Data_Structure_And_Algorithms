class TNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


class ListNode(object):

    def __init__(self, value, pre=None, nxt=None):
        self.value = value
        self.pre = pre
        self.nxt = nxt

    def __repr__(self):
        return str(self.value)


class BTree(object):

    def __init__(self, root: TNode = None):
        self.root = root

    def preOrder(self):
        if self.root is None:
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

    def preOrderRec(self):
        root = self.root
        self._preOrderRec(root)
        print()

    def _preOrderRec(self, root: TNode):
        if root:
            print(root, end=' ')
            self._preOrderRec(root.left)
            self._preOrderRec(root.right)

    def inOrder(self):
        if self.root is None:
            return
        node, stack = self.root, []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                print(node, end=' ')
                node = node.right

    def inOrderRec(self):
        root = self.root
        self._inOrderRec(root)
        print()

    def _inOrderRec(self, root: TNode):
        if root:
            self._inOrderRec(root.left)
            print(root, end=' ')
            self._inOrderRec(root.right)

    def postOrder(self):
        if self.root is None:
            return
        prev, stack = None, [self.root]
        while stack:
            curr = stack[-1]
            # 3 conditions to visit current node
            #   - Current node has no child
            #   - Current node's right child has just been visited
            #   - Current node's left child has just been visited and right child is None
            if curr.left is None and curr.right is None or \
                prev is not None and curr.right == prev or \
                prev is not None and curr.left == prev and curr.right is None:
                node = stack.pop()
                prev = node
                print(node, end=' ')
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        print()

    def postOrderRec(self):
        root = self.root
        self._postOrderRec(root)
        print()

    def _postOrderRec(self, root: TNode):
        if root:
            self._postOrderRec(root.left)
            self._postOrderRec(root.right)
            print(root, end=' ')

    def levelOrder(self):
        if self.root is None:
            return
        currLevel, nextLevel = [self.root], []
        while currLevel:
            node = currLevel.pop()
            print(node, end=' ')
            if node.right:
                nextLevel.append(node.right)
            if node.left:
                nextLevel.append(node.left)
            if len(currLevel) == 0:
                currLevel, nextLevel = nextLevel, currLevel
                print()

    def insert(self, node: TNode):
        if node is None:
            return
        self.root = self._insertRec(self.root, node)

    def _insertRec(self, root: TNode, node: TNode):
        if root is None or root.value == node.value:
            return node
        if root.value > node.value:
            root.left = self._insertRec(root.left, node)
        if root.value < node.value:
            root.right = self._insertRec(root.right, node)
        return root

    def delete(self, node: TNode):
        if self.root is None or node is None:
            return
        self._delete(self.root, node)

    def _delete(self, root: TNode, node: TNode):
        if root is None:
            raise Exception('Try to delete a non-existing value.')
        if root.value > node.value:
            root.left = self._delete(root.left, node)
        elif root.value < node.value:
            root.right = self._delete(root.right, node)
        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                minValueNode = self.minValueNode(root.right)
                root.value = minValueNode.value
                root.right = self._delete(root.right, minValueNode)
        return root

    def minValueNode(self, root: TNode):
        if root is None:
            return root
        while root.left:
            root = root.left
        return root

    def search(self, node: TNode):
        return self._search(self.root, node)

    def _search(self, root: TNode, node: TNode):
        if root is None or node is None:
            return False
        if root.value == node.value:
            return True
        if root.value > node.value:
            return self._search(root.left, node)
        if root.value < node.value:
            return self._search(root.right, node)

    def pathToNode(self, node: TNode):
        if node is not None:
            return self._pathToNode(self.root, node, [self.root])

    def _pathToNode(self, root: TNode, node: TNode, path: list):
        if root is None:
            return
        if root.value == node.value:
            return path
        if root.value > node.value:
            newpath = self._pathToNode(root.left, node, path + [root.left])
            if newpath is not None:
                return newpath
        if root.value < node.value:
            newpath = self._pathToNode(root.right, node, path + [root.right])
            if newpath is not None:
                return newpath

    def lowestCommonAncestor(self, node1: TNode, node2: TNode):
        path1 = self.pathToNode(node1)
        path2 = self.pathToNode(node2)
        if path1 is None or path2 is None:
            return
        index = 0
        while index < len(path1) and index < len(path2):
            if path1[index] != path2[index]:
                break
            index += 1
        return path1[index-1]

    def minHeight(self):
        if self.root is None:
            return 0
        return self._minHeight(self.root, 1)

    def _minHeight(self, root: TNode, currHeight):
        if root.left is None or root.right is None:
            return currHeight
        return min(self._minHeight(root.left, currHeight+1),
                   self._minHeight(root.right, currHeight+1))

    def maxHeight(self):
        if self.root is None:
            return 0
        return self._maxHeight(self.root, 0)

    def _maxHeight(self, root: TNode, currHeight):
        if root is None:
            return currHeight
        if root.left is None:
            return self._maxHeight(root.right, currHeight+1)
        if root.right is None:
            return self._maxHeight(root.left, currHeight+1)
        return max(self._maxHeight(root.left, currHeight+1),
                   self._maxHeight(root.right, currHeight+1))

    def isBalance(self):
        if self.maxHeight() - self.minHeight() <= 1:
            return True
        return False

    def fromPreOrderAndInOrder(self, preorder: list, inorder: list):
        self.root = self._fromPreOrderAndInOrder(preorder, inorder)

    def _fromPreOrderAndInOrder(self, preorder: list, inorder: list):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TNode(inorder[idx])
            root.left = self._fromPreOrderAndInOrder(preorder, inorder[:idx])
            root.right = self._fromPreOrderAndInOrder(preorder, inorder[idx+1:])
            return root

    def fromInOrderAndPostOrder(self, inorder: list, postorder: list):
        self.root = self._fromPreOrderAndInOrder(inorder, postorder)

    def _fromInOrderAndPostOrder(self, inorder: list, postorder: list):
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TNode(inorder[idx])
            root.right = self._fromInOrderAndPostOrder(inorder[:idx], postorder)
            root.right = self._fromInOrderAndPostOrder(inorder[idx+1:], postorder)
            return root

    def toDoubleLinkedList(self):
        self._head, self._prev = None, None
        self._inorderConvert(self.root)
        return self._head

    _head, _prev = None, None

    def _inorderConvert(self, root: TNode):
        if root:
            self._inorderConvert(root.left)
            # Do some stuff here
            if self._head is None:
                self._head = self._prev = ListNode(root.value)
            else:
                if self._head == self._prev:
                    self._head.nxt = root
                    self._prev = root
                    self._prev.pre = self._head
                else:
                    self._prev.nxt = root
                    tmp = self._prev
                    self._prev = root
                    self._prev.pre = tmp
            self._inorderConvert(root.right)
