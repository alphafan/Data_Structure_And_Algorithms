# Delete a node in linked list

```python
# A simple Implementation of Linked List


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
    # Delete element(s)
    # ---------------------------------------------

    def delete(self, value):
        """ Delete the first node with value """
        if self.head is None:
            raise Exception('Empty List')
        if self.head.value == value:
            self.head = self.head.next
            return self
        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return self
            node = node.next
            if node is None:
                break
        return self

    def deleteAll(self, value):
        """ Delete all nodes with the value in list """
        if self.head is None:
            raise Exception('Empty List')
        while self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                return self
        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
            else:
                node = node.next
            if node is None:
                return self
        return self

    def deleteAt(self, k):
        """ Delete a node at index k """
        if self.head is None:
            raise Exception('Empty list')
        if k < 0:
            raise Exception('Delete position can not be negative')
        if k == 0:
            self.head = self.head.next
            return self
        i, node = 0, self.head
        while i < k:
            node = node.next
            i += 1
            if node.next is None:
                raise Exception('Position k: ({}) out of range'.format(k))
        if node.next is None:
            raise Exception('Position k: ({}) out of range'.format(k))
        node.next = node.next.next
        return self

```