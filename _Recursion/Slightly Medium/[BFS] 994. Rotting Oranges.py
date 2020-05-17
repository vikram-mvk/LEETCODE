'''
https://leetcode.com/problems/rotting-oranges/

first we need to add all the rotten oranges in a queue
then perform BFS on the queue elements: i.e., if an adjacent is fresh, make it rot

'''

class Solution:
    mins = 0
    rotten = 0
    qlen = 0
    s=set()

    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = []
        total = len(grid) * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    total -= 1
                if grid[i][j] == 2:
                    self.rotten += 1
                    q.append((i, j))
        self.bfs(grid, q, total)

        if self.rotten == total:
            return self.mins
        if total > self.rotten:
            return -1

        return 0

    def bfs(self, grid, q, total):
        self.qlen = len(q)

        while len(q) > 0:
            if self.qlen == 0:
                self.mins += 1

                self.qlen = len(q)

            temp = q.pop(0)

            if self.rot(grid, temp[0], temp[1] + 1): q.append((temp[0], temp[1] + 1))
            if self.rot(grid, temp[0] + 1, temp[1]): q.append((temp[0] + 1, temp[1]))
            if self.rot(grid, temp[0], temp[1] - 1): q.append((temp[0], temp[1] - 1))
            if self.rot(grid, temp[0] - 1, temp[1]): q.append((temp[0] - 1, temp[1]))

            self.qlen -= 1

    def rot(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 2
            self.rotten += 1
            return True
        else:
            return False









