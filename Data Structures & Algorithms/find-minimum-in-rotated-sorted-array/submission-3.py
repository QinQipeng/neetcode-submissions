class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # the mid belongs to the larger portion of the rotated sorted array
                left = mid + 1
            else:
                right = mid
        return nums[left]