class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.insert(0, data)

    def is_empty(self):
        return self.stack == []

    def pop(self):
        """check if stack is empty
        do nothing; otherwise, remove the val at the index
        """
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)


s_1 = Stack()
s_1.push("Name")
s_1.push("Name")
print(s_1.size())
print(s_1.peek())
print("Just popped: {}".format(s_1.pop()))
print("Just popped: {}".format(s_1.pop()))
print("Just popped: {}".format(s_1.pop()))
print("Just popped: {}".format(s_1.pop()))
