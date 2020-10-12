'''
2 solutions
DP and expand around center
https://medium.com/@edward.zhou/5-longest-palindromic-substring-graphically-explained-python3-solution-76c75e171e15

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        if lenS == 0: return ''
        res = s[0]

        # trick 1
        dp = [[False for i in range(lenS)] for j in range(lenS)]

        # trick 2
        for i in range(lenS):
            dp[i][i] = 1 #length =1  palindrome
            if (i < lenS - 1) and (s[i] == s[i + 1]): #length = 2  palindrome
                dp[i][i + 1] = True
                res = s[i:i + 1 + 1]

        for pos in range(2, lenS):
            row = 0
            col = pos
            for row in range(0, lenS - pos):
                # to judge if dp[row][col] is palindromic , let's check
                #   if dp[row+1][col-1] is palindromic AND s[row]==s[col]
                #   then dp[row][col] is palindromic
                if dp[row + 1][col - 1] and s[row] == s[col]:
                    dp[row][col] = True
                    res = s[row:col + 1]
                col += 1
        return res

def longestPalindrome(self, s: str) -> str:
    if not s: return ""
    start = end = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    curr_len = 1
    for i in range(len(s)):
        temp = curr_len
        curr_len = max(expand(i, i), expand(i, i + 1), curr_len)
        if curr_len > temp:
            start = i - (curr_len - 1) // 2
            end = i + curr_len // 2  # from middle go half the curr_len

    return s[start:end + 1]





