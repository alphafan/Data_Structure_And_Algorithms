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


def flatten(head: ListNode):
    if head is None:
        return head
    node = head
    while node:
        right = node.right
        _, tail = merge(node)
        tail.right = right
        node = right
    return head


def merge(head: ListNode):
    node = head
    tail = None
    while node:
        node.right = node.child
        child = node.child
        tail = node
        node.child = None
        node = child
    return head, tail


a, b, c, d, e, f, g = (ListNode(i) for i in 'abcdefg')
a.right = d
a.child = b
b.child = c
d.right = g
d.child = e
e.child = f


a = flatten(a)
print(a)
