'''
If the first letter matches the character in matrix call dfs from there.
We shouldn't use the same letter that was previously visited. so have a visited set to add the indices at each call
after one of the recursive call has returned a value to the found variable in the caller, remove the visited entry for that


'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, ptr, visited):
            if ptr == len(word): return True
            if (i, j) in visited or i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or word[ptr] != board[i][j]: return False

            visited.add((i, j))
            found = dfs(i, j + 1, ptr + 1, visited) or dfs(i + 1, j, ptr + 1, visited) or dfs(i, j - 1, ptr + 1,visited) or dfs(i - 1, j, ptr + 1, visited)
            visited.remove((i, j))
            return found

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(i, j, 0, set()): return True

        return False


