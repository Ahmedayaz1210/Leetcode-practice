class MinStack:

    def __init__(self):
        self.stack = []
        self.mem = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mem:
            self.mem.append(min(self.mem[-1], val))
        else:
            self.mem.append(val)


    def pop(self) -> None:
        self.mem.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mem[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()