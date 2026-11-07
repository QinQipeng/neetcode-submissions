from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        sMap: dict[str, int] = collections.defaultdict(int)

        L, have, need = 0, 0, len(tMap)
        res_len = float("inf")
        best_L, best_R = 0, 0
        for R in range(len(s)):
            c = s[R]
            sMap[c] += 1

            if sMap[c] == tMap[c]:
                have += 1
            while have == need:
                if (R - L + 1) < res_len:
                    res_len = R - L + 1
                    best_L, best_R = L, R

                if sMap[s[L]] == tMap[s[L]]:
                    have -= 1
                sMap[s[L]] -= 1
                L += 1

        return s[best_L: best_R + 1] if res_len != float("inf") else ""