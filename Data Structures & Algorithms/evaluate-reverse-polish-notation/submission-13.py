class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                a, b = int(stack.pop()), int(stack.pop())
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(a*b)
                elif t == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack.pop()