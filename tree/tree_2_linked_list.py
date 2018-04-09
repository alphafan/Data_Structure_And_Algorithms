""" Convert a BST to a sorted doubly linked list in place. """


class TreeNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


head = None
prev = None


def toLinkedList(root):
    global head

    def toLinkedListHelper(root):
        global head, prev
        # In order visit
        if root:
            toLinkedListHelper(root.left)
            if prev is None:
                head = root
            else:
                prev.right = root
                root.left = prev
            prev = root
            toLinkedListHelper(root.right)

    toLinkedListHelper(root)


a, b, c, d, e, f, g = (TreeNode(i) for i in 'abcdefg')
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

toLinkedList(a)
print(head.value)
