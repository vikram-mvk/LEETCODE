'''
https://leetcode.com/problems/unique-paths/





'''

m=3
n=2
dp = [[0] * m for i in range(n)]
i = 0
j = 0
while i < n:
    dp[i][0] = 1
    i += 1
while j < m:
    dp[0][j] = 1
    j += 1

i = 1
j = 1
while i < n:
    j=1
    while j < m:
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        j+=1
    i+=1
print(dp[i-1][j-1])