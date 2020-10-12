class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        i = j = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] == 0:
                    for x in range(len(matrix)):  matrix[x][j] = float('inf') if matrix[x][j] != 0 else 0
                    for y in range(len(matrix[i])):  matrix[i][y] = float('inf') if matrix[i][y] != 0 else 0
                j += 1
            i += 1

        i = j = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
                j += 1
            i += 1
