class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            anag = "".join(sorted(s))
            anagrams.setdefault(anag,[])
            anagrams[anag].append(s)
        return [val for val in anagrams.values()]