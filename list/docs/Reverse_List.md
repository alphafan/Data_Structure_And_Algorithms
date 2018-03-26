# Reverse a linked list

```python
class List(object):

    def reverse(self):
        """ Reverse the list """
        if self.head is None:
            return self
        pre, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        self.head = pre
        return self

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        repr_str, node = '', self.head
        while node:
            repr_str += str(node) + ' -> '
            node = node.next
        return repr_str + 'None'
        

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
```