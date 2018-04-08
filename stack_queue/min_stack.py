import random


class MinStack(object):

    def __init__(self):
        self.data = []
        self.minValue = 0

    def push(self, value):
        if len(self.data) == 0:
            self.data.append(value)
            self.minValue = value
        else:
            if value < self.minValue:
                self.data.append(value * 2 - self.minValue)
                self.minValue = value
            else:
                self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return
        topValue = self.data.pop()
        if topValue < self.minValue:
            popValue = self.minValue
            self.minValue = topValue * 2 - self.minValue
            return popValue
        else:
            popValue = topValue
        return popValue

    def min(self):
        if len(self.data) == 0:
            return
        return self.minValue


stack = MinStack()
for i in range(10):
    num = random.randint(1, 10)
    print(num, end=' ')
    stack.push(num)
print()
for i in range(10):
    num = stack.pop()
    print(num, end=' ')
print()
