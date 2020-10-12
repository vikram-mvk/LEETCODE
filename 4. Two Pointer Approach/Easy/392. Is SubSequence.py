class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        count = 0
        i = 0
        j = 0
        while j < len(s) and i < len(t):
            if t[i] == s[j]:
                count += 1
                j += 1
            i += 1

        return count == len(s)
