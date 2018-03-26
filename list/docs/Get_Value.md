# Get node value in linked list

```python
class List(object):

    def get(self, k):
        """ Get the node value at k position """
        if self.head is None and k != 0:
            raise Exception('Empty List')
        if k < 0:
            raise Exception('Position k: ({}) can not be negative'.format(k))
        if k == 0:
            return self.head
        i, node = 0, self.head
        while i < k:
            node = node.next
            i += 1
            if node is None:
                raise Exception('k: ({}) out of range'.format(k))
        return node.value

    def getMidItem(self):
        if self.head is None or self.head.next is None:
            return None
        slow, fast = self.head, self.head
        while slow and fast:
            if fast.next is None:
                break
            fast = fast.next.next
            if fast is None:
                break
            slow = slow.next
        return slow

    def getKthLast(self, k):
        """ Return the last Kth value. """
        if k < 0:
            raise Exception('Position k: ({}) can not be negative'.format(k))
        if self.head is None and k != 0:
            raise Exception('k out of range')
        if self.head is None and k == 0:
            return None
        i, fast, slow = 0, self.head, self.head
        while i < k:
            fast = fast.next
            i += 1
            if fast is None and i != k:
                raise Exception('Position k: ({}) out of range'.format(k))
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        repr_str, node = '', self.head
        while node:
            repr_str += str(node) + ' -> '
            node = node.next
        return repr_str + 'None'
    
 
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
```