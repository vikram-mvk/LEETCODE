'''
https://leetcode.com/problems/single-number/solution/

See solution 4
'''


def singleNumber(self, nums: List[int]) -> int:
    a = 0
    for i in nums:
        a = a ^ i
        print(a)
    return a