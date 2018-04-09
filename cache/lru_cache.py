""" LRU Cache Implementation using Double Linked List"""


class ListNode(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.key2node = dict()
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self):
        reprStr = ''
        node = self.head.next
        while node != self.tail:
            reprStr += '{}: {} '.format(node.key, node.value)
            node = node.next
        return reprStr

    def get(self, key):
        if key in self.key2node:
            node = self.key2node[key]
            self._remove(node)
            self._add(node)
            return node.value

    def add(self, key, value):
        node = ListNode(key, value)
        if key in self.key2node:
            self._remove(self.key2node[key])
            self._add(node)
        else:
            self._add(node)
        self.key2node[key] = node
        if len(self.key2node) > self.capacity:
            node = self.head.next
            self.head.next = node.next
            node.next.prev = self.head
            del self.key2node[node.key]

    def _remove(self, node):
        prev = node.prev
        post = node.next
        prev.next = post
        post.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


cache = LRUCache(5)
cache.add(1, 2)
cache.add(2, 4)
cache.add(3, 8)
cache.add(4, 8)
cache.add(5, 8)
cache.add(6, 8)
cache.add(7, 8)
cache.add(8, 8)
print(cache)
print(cache.get(1))
