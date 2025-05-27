class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

        return -1

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]

        return -1