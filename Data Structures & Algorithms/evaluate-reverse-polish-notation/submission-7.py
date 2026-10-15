class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                a, b = int(numStack.pop()), int(numStack.pop())
                if t == "+":
                    numStack.append(a+b)
                elif t == "-":
                    numStack.append(b-a)
                elif t == "*":
                    numStack.append(a*b)
                elif t == "/":
                    numStack.append(int(b / a))
            else:
                numStack.append(int(t))
        return numStack.pop()