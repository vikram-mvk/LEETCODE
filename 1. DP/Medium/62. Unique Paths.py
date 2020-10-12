'''
https://leetcode.com/problems/unique-paths/

Main idea:
the number of ways to go to the last grid is the sum of the number of ways to go to the pre row of last grid and
pre column of last grid

So find the number of ways to go to each grid from the starting point


'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is cols and n is rows
        dp = [[1] * (m + 1) for x in range(n + 1)]
        #create one more extra row and column to store intial values which helps to start the dp

        for rows in range(1, n):
            for cols in range(1, m):
                dp[rows][cols] = dp[rows - 1][cols] + dp[rows][cols - 1]
                #curr row col value is pre row same col + pre col same row

        return dp[n - 1][m - 1]