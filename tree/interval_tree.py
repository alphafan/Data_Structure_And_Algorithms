""" Interval Tree """

import sys


class Interval(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high


class TreeNode(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max = -sys.maxsize
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}-{}-{}'.format(self.low, self.high, self.max)


class IntervalTree(object):

    def levelVisit(self, root):
        if root is None:
            return
        currLevel, nextLevel = [root], []
        while currLevel:
            while currLevel:
                node = currLevel.pop(0)
                print(node, end=' ')
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            print()
            currLevel, nextLevel = nextLevel, currLevel

    def addInterval(self, root, interval: Interval):
        if root is None:
            root = TreeNode(interval.low, interval.high)
        else:
            if interval.low < root.low:
                root.left = self.addInterval(root.left, interval)
            else:
                root.right = self.addInterval(root.right, interval)
        root.max = max(root.high, interval.high)
        root = self.reBalance(root)
        return root

    def getHeight(self, root):
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.getHeight(root.right)
        if root.right is None:
            return 1 + self.getHeight(root.left)
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def reBalance(self, root):
        if root is None:
            return root
        while self.getHeight(root.left) < self.getHeight(root.right):
            root = self.leftRotate(root)
        while self.getHeight(root.left) > self.getHeight(root.right):
            root = self.rightRotate(root)
        return root

    def leftRotate(self, root):
        if root is None or root.right is None:
            return root
        right = root.right
        root.right = right.left
        right.left = root
        return right

    def rightRotate(self, root):
        if root is None or root.left is None:
            return root
        left = root.left
        root.left = left.right
        left.right = root
        left.max = max(left.high, left.left.max, left.right.max)
        root.max = max(root.high, root.left.max, root.right.max)
        return left


tree = IntervalTree()
root = TreeNode(1, 3)
root = tree.addInterval(root, Interval(2, 4))
root = tree.addInterval(root, Interval(0, 4))
root = tree.addInterval(root, Interval(1, 9))
root = tree.addInterval(root, Interval(6, 8))
root = tree.addInterval(root, Interval(5, 7))
tree.levelVisit(root)
