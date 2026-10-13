class Solution:
    def isValid(self, s: str) -> bool:
        validPairs = {')':'(','}':'{',']':'['}
        bracStack = []
        
        for c in s:
            if c in validPairs:
                if len(bracStack) == 0: return False
                if bracStack.pop() != validPairs[c]: return False
            else:
                bracStack.append(c)
        return len(bracStack) == 0