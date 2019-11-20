class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
    
    def peek(self):
        self.removeCheck()
        return self.data[-1]

    def pop(self):
        element = self.peek()
        self.data = self.data[:-1]
        return element

    def isEmpty(self):
        return len(self.data) == 0

    def removeCheck(self):
        if self.isEmpty(): raise Exception('No elements in stack')