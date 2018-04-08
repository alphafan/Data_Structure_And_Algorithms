""" Tree given with 2 nodes having same child. Find that sort of thing in tree. """


class TNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def getChildren(root):
    if root is None:
        return set()
    children = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
            children.add(node.right)
        if node.left:
            stack.append(node.left)
            children.add(node.left)
    return children


def twoParentsNode(root):
    if root is None:
        return
    leftChildren = getChildren(root.left)
    rightChildren = getChildren(root.right)
    commonNodes = leftChildren.intersection(rightChildren)
    if commonNodes:
        print(commonNodes)
        return
    if root.left:
        twoParentsNode(root.left)
    if root.right:
        twoParentsNode(root.right)


a, b, c, d, e, f, g = (TNode(i) for i in 'abcdefg')
a.left, a.right = b, c
b.left, b.right = d, f
c.left, c.right = f, g

twoParentsNode(a)

