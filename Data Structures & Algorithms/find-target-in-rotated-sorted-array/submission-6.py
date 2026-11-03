class Solution:
    def binarySearch(self, left, right, nums, target) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1


    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        pivot = L
        leftPortion = self.binarySearch(0, pivot - 1, nums, target)
        rightPortion = self.binarySearch(pivot, len(nums) - 1, nums, target)
        return leftPortion if leftPortion > -1 else rightPortion
        