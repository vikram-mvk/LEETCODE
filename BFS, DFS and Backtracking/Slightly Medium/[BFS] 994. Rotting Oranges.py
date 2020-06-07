'''
https://leetcode.com/problems/rotting-oranges/

first we need to add all the rotten oranges in a queue
then perform BFS on the queue elements: i.e., if an adjacent is fresh, make it rot

'''
class Solution:
    mins = 0
    rotten = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        # Queue to use for BFS

        total = len(grid) * len(grid[0])
        # Total No.of Grids

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    total -= 1
                    # Total number of oranges(both fresh and rotten)

                if grid[i][j] == 2:
                    self.rotten += 1
                    q.append((i, j))
                    # append all the rotten oranges in a quque

        # Perform BFS on Q elts
        self.bfs(grid, q, total)

        # finally we check if all oranges are rotten. If yes return Mins.
        if self.rotten == total:
            return self.mins

        # if some oranges can't be rotten, return -1
        if total > self.rotten:
            return -1

        # in anyother case return 0
        return 0


    def bfs(self, grid, q, total):
        qlen = len(q)
        # we use qlen to calculate minutes. 1 minute is passed when the queue elements become empty.
        # in other words, when all the rotten oranges in the queue has affected its neighboring fresh oranges

        while len(q) > 0:

            if qlen == 0:
                self.mins += 1
                qlen = len(q)
                # newly rotten oranges are added to the queue and the length is reassigned to the new length

            temp = q.pop(0)

            # Move in all directions. If an orange is affected, it returns true and this orange can further affect other fresh oranges
            # so add it in the queue
            if self.rot(grid, temp[0], temp[1] + 1): q.append((temp[0], temp[1] + 1))
            if self.rot(grid, temp[0] + 1, temp[1]): q.append((temp[0] + 1, temp[1]))
            if self.rot(grid, temp[0], temp[1] - 1): q.append((temp[0], temp[1] - 1))
            if self.rot(grid, temp[0] - 1, temp[1]): q.append((temp[0] - 1, temp[1]))

            qlen -= 1
        # reduce the previous Qlen. Note the q.append() doesn't have any effect on qlen variable. It denotes the qlen of the previous iteration


    def rot(self, grid, i, j):
        # if i,j is valid and the orange is fresh, rot it and return True.
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:

            grid[i][j] = 2
            self.rotten += 1
            return True
        else:
            return False








