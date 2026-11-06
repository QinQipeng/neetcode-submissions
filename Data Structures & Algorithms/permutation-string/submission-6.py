class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s2Table: dict[str, int] = collections.defaultdict(int)
        s1Table = collections.Counter(s1)

        matches = sum(s1Table[chr(ord('a') + i)] == s2Table[chr(ord('a') + i)] for i in range(26))
        
        L = 0
        for R in range(len(s2)):
            if matches == 26:
                return True

            if R - L + 1 > len(s1):
                if s1Table[s2[L]] == s2Table[s2[L]]:
                    matches -= 1
                s2Table[s2[L]] -= 1
                if s1Table[s2[L]] == s2Table[s2[L]]:
                    matches += 1
                L += 1

            if s1Table[s2[R]] == s2Table[s2[R]]:
                matches -= 1
            s2Table[s2[R]] += 1
            if s1Table[s2[R]] == s2Table[s2[R]]:
                matches += 1

        return matches == 26
            