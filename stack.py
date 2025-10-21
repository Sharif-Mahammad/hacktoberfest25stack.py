class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)  # ❌ Wrong direction — should append at the end

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)  # ❌ Removes wrong element
        return None

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Expected 3, Got 1
