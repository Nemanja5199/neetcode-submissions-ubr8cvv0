class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        newStack = self.stack.copy()
        minV = newStack[-1]
        newStack.pop()
        while newStack:
            minV= min(newStack[-1],minV)
            newStack.pop()
        
        return minV


           


        
