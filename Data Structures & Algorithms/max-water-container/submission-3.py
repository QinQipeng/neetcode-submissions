class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        largest = 0

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            largest = max(largest, area)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return largest
        