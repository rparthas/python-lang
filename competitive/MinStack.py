class MinStack:

    def __init__(self):
        self.elem = []
        self.minelem = []

    def push(self, val: int) -> None:
        if len(self.elem) == 0:
           min_val = val
        else:
            min_val = min(val,self.elem[-1][1])
        self.elem.append((val,min_val))

    def pop(self) -> None:
        self.elem.pop()


    def top(self) -> int:
        return self.elem[-1][0]


    def getMin(self) -> int:
        return self.elem[-1][1]

if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
