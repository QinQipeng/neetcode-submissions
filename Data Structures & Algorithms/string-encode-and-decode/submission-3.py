class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        result, i = [], 0

        while (i < len(s)):
            j = s.find("#", i)

            length = int(s[i:j])
            result.append(s[j+1: j+1+length])
            i = j + 1 + length
        return result