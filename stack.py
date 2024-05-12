class Stack:
    def __init__(self):
        self.data = []

    def push(self, new):
        self.data.append(new)

    def pop(self):
        try:
            rv = self.data.pop()
            return rv
        except IndexError:
            raise IndexError("Tried to pop an empty stack")

    def top(self):
        return self.data[-1]
