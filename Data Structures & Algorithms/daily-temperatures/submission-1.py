class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [index, temperature]

        for idx, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][1]:
                stackIdx, stackTmp = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append([idx, tmp])
        return res