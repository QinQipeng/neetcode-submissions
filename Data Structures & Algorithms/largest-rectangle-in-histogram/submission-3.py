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
        
        while stack:
            i, h = stack.pop()
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)

        return maxArea