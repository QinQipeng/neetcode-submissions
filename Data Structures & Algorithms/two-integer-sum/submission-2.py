class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]], i]
            diff[target-nums[i]] = i