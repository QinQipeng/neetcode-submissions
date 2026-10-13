class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list);
        for s in strs:
            anag = "".join(sorted(s))
            anagrams[anag].append(s)
        return [strlist for strlist in anagrams.values()]