class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {c: s.count(c) for c in s }
        
        for chr in t:
            if (not charDict.get(chr)): return False
            charDict[chr] -= 1
        
        result = set(charDict.values())
        return len(result) == 1 and not any(result)