class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # [idx, hgt]

        for idx, hgt in enumerate(heights):
            start = idx # Left border of the rec
            while stack and stack[-1][1] > hgt:
                i, h = stack.pop()
                maxArea = max(maxArea, h * (idx - i))
                start = i
            stack.append([start, hgt])

        for idx, hgt in stack:
            maxArea = max(maxArea, hgt * (len(heights) - idx))
        
        return maxArea