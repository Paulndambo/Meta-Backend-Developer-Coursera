class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)


s = Stack()
s.push(0)
s.push(2)
s.push(3)
#s.print_stack()
s.is_empty()