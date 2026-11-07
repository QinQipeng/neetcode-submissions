class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and nums[i] == nums[i-1]: continue
            if a > 0: return res
            j, k = i + 1, len(nums) - 1
            while(j < k):
                if nums[j] + nums[k] > -a:
                    k -= 1
                elif nums[j] + nums[k] < -a:
                    j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res