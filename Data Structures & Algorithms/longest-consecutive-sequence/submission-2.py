class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums): return 0

        nums_set = set(nums)
        table = {}

        for n in nums:
            if n-1 not in nums_set:
                length = 1
                while n+length in nums_set:
                    length += 1
                table[n] = length
        
        return max(table.values())


        