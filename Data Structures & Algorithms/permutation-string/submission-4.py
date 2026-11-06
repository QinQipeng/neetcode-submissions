class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s2Table: dict[str, int] = collections.defaultdict(int)
        s1Table = dict(collections.Counter(s1))
        L = 0

        for R in range(len(s2)):
            if s1Table == dict(s2Table):
                return True
            if R - L + 1 > len(s1):
                s2Table[s2[L]] -= 1
                if s2Table[s2[L]] == 0:
                    s2Table.pop(s2[L])
                L += 1
            s2Table[s2[R]] += 1
        
        return s1Table == dict(s2Table)
            