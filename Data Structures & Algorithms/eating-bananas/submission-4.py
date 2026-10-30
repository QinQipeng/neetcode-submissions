from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hour = sum([ceil(p / k) for p in piles])
            if hour <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        return res