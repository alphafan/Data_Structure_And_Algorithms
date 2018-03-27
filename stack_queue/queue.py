from .stack import Stack


class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __repr__(self):
        return '{} {}'.format(self.stack1.data, self.stack2.data)

    def push(self, item):
        self.stack1.push(item)

    def pop(self):
        if self.stack2.size() == 0:
            if self.stack1.size() == 0:
                raise Exception('Empty Queue')
            while self.stack1.size() != 0:
                item = self.stack1.pop()
                self.stack2.push(item)
        return self.stack2.pop()