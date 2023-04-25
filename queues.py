class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue("Car")
q.enqueue("House")
q.enqueue("Cow")
q.print_queue()
q.dequeue()
q.print_queue()