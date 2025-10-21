class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # ✅ Push to end

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # ✅ Pop from end (LIFO)
        return None

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # ✅ Expected 3
