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
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        print(pivot)

        left, right = 0, len(nums) - 1
        leftSearch = self.binarySearch(left, pivot, nums, target)

        return leftSearch if leftSearch != -1 else self.binarySearch(pivot, right, nums, target)
