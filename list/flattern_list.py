""" Flatten List """


class ListNode(object):

    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.child = None

    def __repr__(self):
        node, reprStr = self, ''
        while node:
            reprStr += str(node.value) + ' -> '
            node = node.right
        return reprStr + 'None'


a, b, c, d, e, f, g = (ListNode(i) for i in 'abcdefg')
a.right = d
a.child = b
b.child = c
d.right = g
d.child = e
e.child = f


def flatten(head: ListNode):
    node = head
    while node:
        temp = node.right
        _, tail = merge(node, node.child)
        if tail is None:
            return head
        tail.right = temp
        node = temp


def merge(head, child):
    head.right = child
    head.child = None
    tail = None
    while child:
        child.right = child.child
        child.child = None
        tail = child
        child = child.right
    return head, tail


a = flatten(a)
print(a)