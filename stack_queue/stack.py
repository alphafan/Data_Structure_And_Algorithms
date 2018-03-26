# A python implementation of stack using python list


class Stack(object):

    def __init__(self):
        self.data = []
        self.minValues = []

    def __repr__(self):
        return 'Data: {} Min Values: {}'.format(self.data, self.minValues)

    def size(self):
        return len(self.data)

    def push(self, item):
        if len(self.data) == 0:
            self.minValues.append(item)
        else:
            if item < self.minValues[-1]:
                self.minValues.append(item)
            else:
                self.minValues.append(self.minValues[-1])
        self.data.append(item)

    def top(self):
        if len(self.data) == 0:
            raise Exception('Empty Stack')
        return self.data[-1]

    def pop(self):
        if len(self.data) == 0:
            raise Exception('Empty Stack')
        self.minValues.pop()
        return self.data.pop()

    def minValue(self):
        if len(self.minValues) == 0:
            raise Exception('Empty Stack')
        return self.minValues[-1]
