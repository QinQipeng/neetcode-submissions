class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while (L < R):
            mid = int((L + R) / 2)
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid
            else:
                return mid
        return L if nums[L] == target else -1