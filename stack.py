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

    def dup(self):
        self.push(self.top())

    def swap(self):
        t1 = self.pop()
        t2 = self.pop()
        self.push(t1)
        self.push(t2)

    def add(self):
        self.push(self.pop() + self.pop())

    def sub(self):
        t1 = self.pop()
        t2 = self.pop()
        self.push(t2 - t1)

    def mul(self):
        self.push(self.pop() * self.pop())

    def div(self):
        t1 = self.pop()
        t2 = self.pop()
        self.push(t2 / t1)





