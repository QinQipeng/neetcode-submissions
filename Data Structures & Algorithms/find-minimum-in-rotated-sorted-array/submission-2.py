class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l]) # min to handle the edge case where res is already the minimum
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]: # if l and mid in the same segment, then the minimum will be on the right part
                l = mid + 1
            else:
                r = mid - 1
        return res