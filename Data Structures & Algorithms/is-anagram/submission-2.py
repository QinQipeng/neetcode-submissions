class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {c: s.count(c) for c in s }
        # for chr in s:
        #     charDict.setdefault(chr, 0)
        #     charDict[chr] += 1
        print(charDict)
        
        for chr in t:
            if (not charDict.get(chr)): return False
            charDict[chr] -= 1
        
        result = set(charDict.values())
        return len(result) == 1 and not any(result)