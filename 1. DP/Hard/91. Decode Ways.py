'''
Recursive solution with Tree Pruning
https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0

        def dfs(string, memo):

            if string in memo: return memo[string]

            if len(string) > 0 and string[0] == '0':   return 0

            if string == "" or len(string) == 1:   return 1

            if int(string[0:2]) <= 26:
                memo[string] = dfs(string[1:], memo) + dfs(string[2:], memo)
                return memo[string]
            else:
                return dfs(string[1:], memo)

        return dfs(s, {})

#same soln using while loop
class Solution(object):
    def numDecodings(self, s):
        def search(s, memo):
            if s in memo:   return memo[s]
            if len(s) <= 1: return 1 if s != "0" else 0
            res, n, i = 0, len(s), 1
            while i <= n and 1 <= int(s[:i]) <= 26:
                res += search(s[i:], memo)
                i += 1
            memo[s] = res
            return res
        if s == "": return 0
        return search(s, {})

#Iterative DP solution
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    prev, curr = 1, 1  # prev = s[i-2], curr = s[i-1], initialized to 1
    for i in range(1,len(s)):
        # letter 0 is not allowed, set curr to 0
        if s[i] == '0':
            curr = 0
        # two letters case
        if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
            tmp = curr
            curr += prev  # curr is the sum of curr and prev
            prev = tmp  # old curr
        # one letter case, so no change
        else:
            prev = curr  # no change
    return curr