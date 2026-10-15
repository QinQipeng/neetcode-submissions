class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        table = dict()
        numSet = set(nums) # Removes duplicates

        for n in numSet:
            if not n-1 in numSet: # a potential head
                ind, length = n, 0
                while ind in numSet:
                    length += 1
                    ind += 1

                table[n] = length
        
        return max(table.values())

        