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

    # ---------------------------------------------
    # Get value
    # ---------------------------------------------

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

    # ---------------------------------------------
    # Reverse list element(s)
    # ---------------------------------------------

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


a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c
lst = List(a)
print(lst.isCircular())
