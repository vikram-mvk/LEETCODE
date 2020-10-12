'''
    duplicate avoidance
    Same number can't be used again unless there is another instance of it in the array
    duplicate combinatins must be avoided similar to three sum
    Sort the array, and when pre is same as current, it gonna find the same combination again, so skip
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        pre = [float('inf')]

        def solve(target, curr, index):
            if target == 0: return True
            if target < 0: return False

            while index < len(candidates) - 1:
                index += 1
                if pre[0] == candidates[index]: continue

                if solve(target - candidates[index], curr + [candidates[index]], index):
                    ans.append(curr + [candidates[index]])

                pre[0] = candidates[index]

            return False

        candidates.sort()
        solve(target, [], -1)

        return ans
#With Array Slicing
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        pre = [float('inf')]

        def solve(target, curr, index):
            if target == 0: return True
            if target < 0: return False

            for i, x in enumerate(candidates[index:]):  # slice the array each time to avoid using the same number for the combination
                index += 1  # store the real index, because due to slicing i will always start with 0
                if pre[0] == x: continue
                if solve(target - x, curr + [x], index):  ans.append(
                    curr + [x])  # if recursive call returns true, append it
                pre[0] = x  # store previous to avoid forming the same combo (duplicate)

            return False

        candidates.sort()
        solve(target, [], 0)

        return ans