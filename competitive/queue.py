class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.in_s = Stack()
        self.out_s = Stack()

    def push(self,ele):
        self.in_s.push(ele)

    def pop(self):
        self.__shift_stack()
        return self.out_s.pop()

    def peek(self):
        self.__shift_stack()
        return self.out_s.peek()

    def is_empty(self):
        return self.in_s.size() + self.out_s.size() == 0

    def size(self):
        return self.in_s.size() + self.out_s.size()

    def __shift_stack(self):
        while not self.in_s.is_empty():
            self.out_s.push(self.in_s.pop())


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.is_empty())  # Output: False
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())  # Output: 3
    print(queue.peek())  # Output: 2
    print(queue.is_empty())  # Output: False
    print(queue.pop())
    print(queue.size())
