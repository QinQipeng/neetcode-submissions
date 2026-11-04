class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, length = 0, 0
        window = set()

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            length = max(length, R - L + 1)
            window.add(s[R])
        return length