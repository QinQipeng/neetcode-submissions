class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            map.setdefault(n, 0)
            map[n] += 1
        
        for v in map.values():
            if v > 1:
                return True
        return False
        