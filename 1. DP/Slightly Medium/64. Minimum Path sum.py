'''
Recursive memoization approach:


'''
grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

#Recursion and memoization
dp = {}
def path(i, j):
    if (i, j) in dp: return dp[(i, j)]

    if i >= len(grid) or j >= len(grid[i]): return float('inf')

    if i == len(grid) - 1 and j == len(grid[i]) - 1: return grid[i][j]

    dp[(i, j)] = grid[i][j] + min(path(i + 1, j), path(i, j + 1))

    return dp[(i, j)]

print(path(0, 0))


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # We can get to element in the first column only from the same column's pre row
        for i in range(1, len(grid)):  grid[i][0] += grid[i - 1][0]

        # We can get to element in the first row only from the same row's pre column
        for i in range(1, len(grid[0])): grid[0][i] += grid[0][i - 1]

        # Now we update the inner values
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])  # which path is minimum, from up or left?

        return grid[-1][-1]
