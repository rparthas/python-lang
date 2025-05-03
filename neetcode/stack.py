from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()

    def top(self):
        if len(self.queue) > 0:
            ele = self.queue.pop()
            self.queue.append(ele)
            return ele
        return None

    def empty(self):
        return not self.queue1


if __name__ == "__main__":
    q = MyStack()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.top())
    print(q.pop())
    print(q.pop())
    print(q.pop())
