'''
1. If its odd, add a zero
2. add i and -i until len(ans) is < n

'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 != 0:
            ans.append(0)
            n -= 1
        i = 1
        while len(ans) < n:
            ans.append(i)
            ans.append(-i)
            i += 1
        return ans
