'''
https://leetcode.com/problems/number-of-islands/

if value is 1, island is found. increment count and
trace the border of the island using recursion. (enter condition: if i and j are valid and value[i][j]=='1'
if '1' is found make 0
'''
#One approach is to increment island when you found a '1'
# and trace its border and mark all of it as '0'
def numIslands(self, grid: List[List[str]]) -> int:
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands += 1
                self.search(grid, i, j)
    print(islands)
    return islands


def search(self, grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return

    grid[i][j] = '0'

    self.search(grid, i + 1, j)
    # next row same column
    self.search(grid, i, j + 1)
    # same row next column
    self.search(grid, i - 1, j)
    # previous row same column
    self.search(grid, i, j - 1)
    # same row previous column

