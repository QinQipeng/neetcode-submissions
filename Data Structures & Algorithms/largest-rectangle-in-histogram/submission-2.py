class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # [start, height] 

        for idx, hgt in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > hgt:
                i, h = stack.pop()
                area = h * (idx - i)
                maxArea = max(maxArea, area)
                start = i
            stack.append([start, hgt])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea