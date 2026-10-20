class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [idx, tmp]
        for idx, tmp in enumerate(temperatures):
            while stack and stack[-1][1] < tmp:
                popped = stack.pop()
                res[popped[0]] = idx - popped[0]
            stack.append([idx, tmp])
        return res