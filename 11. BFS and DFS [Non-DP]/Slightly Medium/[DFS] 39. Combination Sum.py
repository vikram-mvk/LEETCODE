'''
Use index as a funciton parameter to pick elements
add those elements if the solve return True
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(target, curr, index):
            if target == 0: return True
            if target < 0: return False

            while index < len(candidates):
                if solve(target - candidates[index], curr + [candidates[index]], index):
                    ans.append( curr + [candidates[index]])
                index += 1
            return False

        solve(target, [], 0)

        return ans

#With slicing
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def solve(target, curr, index):
            if target == 0: return True
            if target < 0: return False

            for i, x in enumerate(candidates[index:]):
                if solve(target - x, curr + [x], index + i): ans.append(curr + [x])

            return False

        solve(target, [], 0)

        return ans