'''
Do not think that we have all the houses at once, initially consider we only have one house.
initial_money is just nums[0]
when we have 2 houses, max(h1,h2) -> max_money
now when there is three, h3+h1 or simply h2 will be the new max_money. initial_money becomes old_max_money

Let's start with describing the structure of an optimal solution in terms of its optimal subproblems.

We want to rob as many houses as we can, but we can't rob adjacent houses. Therefore, given n houses, on our last move we either rob house n or house n - 1 (we can't do both because they are adjacent).
We want to choose the move that gives us the maximum value, so we choose between:

maximum value at house n-1 (we can't add anything else)
maximum value at house n-2 plus value of house n
Which is: f(n) = max(f(n-1), f(n-2) + house[n])
To make this into a recurrence relation, we need the base case:
f(1) = house[0] (if n = 1, we just rob that one house)
f(2) = max(house[0], house[1]) (if n = 2, we choose which one to rob)

Version 1: obvious recursive solution. Exponential; maximum recursion depth exceeded, of course.
'''
def rob(nums):
    def maxval(n):
        if n == 0:
            return nums[0]
        elif n == 1:
            return max(nums[0], nums[1])
        else:
            return max(maxval(n-1), maxval(n-2) + nums[n])

    return maxval(len(nums)-1)
#Version 2: memoization. Instead of computing the same subproblems over and over (see verion 1), compute them once and store the result in a lookup cache. O(n) time (becasue exactly 2 recursive calls for each value) and O(n) space.

def rob(nums):
    def maxval(n):
        if cache[n] is None:
            cache[n] = max(maxval(n-1), maxval(n-2) + nums[n])
        return cache[n]

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    cache = [None] * len(nums)
    cache[0], cache[1] = nums[0], max(nums[0], nums[1])  # load base cases
    return maxval(len(nums)-1)
#Version 3: dynamic programming. Similar to verion 2, but we do it bottom-up: we precompute the lookup cache. O(n) time, O(n) space.

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    cache = [None] * len(nums)
    cache[0], cache[1] = nums[0], max(nums[0], nums[1])  # load base cases
    for i in range(2, len(nums)):
        cache[i] = max(cache[i-1], cache[i-2] + nums[i])
    return cache[len(nums)-1]

#Version 4: same as above, but O(1) space. We don't need to store all the values, we just need n-1 and n-2.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        initial_money = nums[0]
        max_money = max(nums[0], nums[1])

        # there are only two money at any point and decision has to be takes as to which money we must use

        for i in range(2, len(nums)):
            pre_max = max_money
            max_money = max(initial_money + nums[i], max_money)
            initial_money = pre_max

        return max_money