class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurs = {}
        for n in nums:
            occurs.setdefault(n, 0)
            occurs[n] += 1
        
        sorted_occurs = sorted(list(occurs.items()), key=lambda item: item[1], reverse=True)
        return [item[0] for idx, item in enumerate(sorted_occurs) if idx < k]