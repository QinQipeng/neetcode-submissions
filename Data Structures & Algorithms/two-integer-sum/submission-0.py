class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if(not diff.get(nums[i], None) == None):
                return [diff[nums[i]], i]
            diff[target - nums[i]] = i
        return []
