'''
Identification of sub problem:
Tree's right branch recomputes values that are already done in left branch.
So store it with DP and avoid computing right branch

At any given point(n) we can either take 1 step or 2 steps
if n=5
then,
         5
        /  \
       4    3 (already computed, so get from dp)
      /  \
     3    2 (already computed, so get from dp)
    / \  / \
   2   1 1  0
(these 4 values are obtained from dp)
left subtree executes fully.
right subtree gets value from dp
'''
#Top Down recusive approach
class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def climb(n):
            if n in dp: return dp[n]     #if the subtree is already calculated, just return the stored value
            if n<1: return 0             #no way to climb if n<1 so return 0
            if n==1 or n==2: return n    #1 way if n=1 and 2 ways if n=2
            dp[n]=climb(n-1)+climb(n-2)
            return dp[n]
        return climb(n)

#bottom up iterative approach
class Solution:
    def climbStairs(self, n: int) -> int:
        # base conditions
        if n < 1: return 0
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for x in range(3, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]  # the number of ways to go to N is the sum of the number of ways to go to n-1 and n-2

        return dp[n]


# Fibonacci stye reduced space complexity solution
# At a given N, all we want is the value of n-1 and n-2 to compute N.  So we dont need to store the entire array but just 2 variables, pre to store previous and pre_pre to store pre's pre.
class Solution:
    def climbStairs(self, n: int) -> int:
        # base conditions
        if n < 1: return 0
        if n == 1: return 1
        if n == 2: return 2

        # the number of ways to go to N is the sum of the number of ways to go to n-1 and n-2
        # therefore, start from the base condition. if we're at n=3 we need to know how many ways are there to go to n=2 and n=1
        # pre is 2 and pre_pre is 1

        pre_pre = 1
        pre = 2

        curr = -1  # currently we don't know how many ways are there. so initialize to something dummy

        for x in range(3, n + 1):
            curr = pre + pre_pre  # the number of ways to go to N is the sum of the number of ways to go to n-1 and n-2

            pre_pre = pre  # At a given N, all we want is the value of n-1 and n-2 to compute N. Since n is going to increase in the loop, move the pre and pre_pre
            pre = curr

        return curr