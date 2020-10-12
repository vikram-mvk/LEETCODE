'''
1. Create a set with tuple i,j if i,j is zero
2. Loop the matrix and when we find one, add its neighbors to bfs
3. check if each neighbor exist in set, if not remove it from bfs but add its neighbors to the last
4. when the queue's inital size is 0, distance increases by one because in the 1st set of neighbors, we didn't find a zero . so +1


'''
class Solution:
    def updateMatrix(self, matrix):
        zero_pairs = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:  zero_pairs.add((i, j))

        # or set comprehension
        zero_pairs = set((i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0)

        #return valid neighbors
        def get_neighbors(i, j):
            neighbors = []
            if i - 1 >= 0: neighbors.append((i - 1, j))
            if i + 1 < len(matrix): neighbors.append((i + 1, j))
            if j - 1 >= 0: neighbors.append((i, j - 1))
            if j + 1 < len(matrix[i]): neighbors.append((i, j + 1))
            return neighbors


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    bfs = []
                    for elts in get_neighbors(i, j):  bfs.append(elts)
                    distance = 1
                    size = len(bfs)
                    while size > 0:
                        if bfs[0] in zero_pairs:  break
                        else:
                            x, y = bfs.pop(0)
                            for elts in get_neighbors(x, y):  bfs.append(elts)
                        size -= 1
                        if size == 0:
                            distance += 1
                            size = len(bfs)

                    matrix[i][j] = distance

        return matrix
