# Insert a node in linked list

```python
class Node(object):

    """ List Node

    Args:
        value: data storing at this node
        next: pointer to the linked node
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class List(object):

    """ List of nodes

    Args:
        head: (Node) Head node of a list
    """

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        repr_str, node = '', self.head
        while node:
            repr_str += str(node) + ' -> '
            node = node.next
        return repr_str + 'None'

    # ---------------------------------------------
    # Insert an element
    # ---------------------------------------------

    def insert(self, value):
        """ Insert a node to the end of list """
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        return self

    def insertAt(self, value, k):
        """ Insert a value at k position """
        if k < 0:
            raise Exception('Insert position should not be negative')
        if self.head is None and k > 0:
            raise Exception('Position k: ({}) out pf range'.format(k))
        if k == 0:
            if self.head is None:
                self.head = Node(value)
                return self
            if self.head is not None:
                node = Node(value)
                node.next = self.head
                self.head = node
                return self
        node, i = self.head, 0
        while i < k-1:
            i += 1
            node = node.next
            if node is None:
                raise Exception('Position k: ({}) out pf range'.format(k))
        next = node.next
        node.next = Node(value)
        node.next.next = next
        return self
```