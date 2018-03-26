# Check if a list is circular

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
    # Check if a list is circular
    # ---------------------------------------------

    def isCircular(self):
        fast, slow = self.head, self.head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False
        
```