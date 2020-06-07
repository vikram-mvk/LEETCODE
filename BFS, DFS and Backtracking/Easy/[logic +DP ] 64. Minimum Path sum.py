'''
Ususally we optimize recursion by storing the values of left subtree call
and reuse these values when building the right sub tree call.
here the right subtree is doesn't have the same computation as the left.
but still, the shortest path is dependent on previous values.
So we use iterative approach.

'''

#with using a 2d DP array (not the best solution)
grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
rows = len(grid) + 1
cols = len(grid[0]) + 1
dp = [[999 for j in range(cols)] for i in range(rows)]
dp[0][1] = 0
dp[1][0] = 0

for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i - 1][j - 1]

print(dp[rows - 1][cols - 1])

#best solution. NO extra space
#Without using extra DP array
#just add a condition when in first row and first column
rows, cols = len(grid), len(grid[0])
for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:  continue  # when we are in 0th row 0th column, don't need to do anything
        if i == 0:
            grid[i][j] = grid[i][j] + grid[i][
                j - 1]  # when we are in 0th row and some other column, we need to add previous column's value
        elif j == 0:
            grid[i][j] = grid[i][j] + grid[i - 1][
                j]  # when we are in 0th column and some other row, we need to add previous row's value
        else:
            grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]  # else we  need to add both the values

print(grid[rows - 1][cols - 1])


'''
Recursive TLE solution
ans = 0
def minPathSum(self, grid: List[List[int]]) -> int:
    def add(i, j, sum):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        if i == len(grid) - 1 and j == len(grid[i]) - 1:
            if sum + grid[i][j] < self.ans: self.ans = sum + grid[i][j]
            return

        if sum+grid[i][j]<self.ans: add(i + 1, j, sum + grid[i][j])
        if sum+grid[i][j]<self.ans: add(i, j + 1, sum + grid[i][j])
        return

    self.ans = 9999
    add(0, 0, 0)
    return self.ans
'''
