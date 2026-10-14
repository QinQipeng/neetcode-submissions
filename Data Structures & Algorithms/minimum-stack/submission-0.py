class MinStack:

    def __init__(self):
        self.stack = []   
        self.prefixMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefixMin.append(min(val, self.prefixMin[-1]) if len(self.prefixMin) else val)

    def pop(self) -> None:
        res = self.stack.pop()
        self.prefixMin.pop()
        return res

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefixMin[-1]
        
