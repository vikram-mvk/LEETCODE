'''
Problem with greedy algorithms
Let's say example [100,99,1] with amount 396. The optimal solution is obviously 4(99 * 4)
but your greedy algorithm will stop and return to root from the first result 99 (100 * 3 + 1 * 96), which is not optimal.
The greedy algorithm(the more bigger coins we use, the less count we need) doesn't work actually.
Another example
https://leetcode.com/problems/coin-change/discuss/77387/Why-this-backtracking-algorithm-doesn't-work-Please-help-methanks-very-much!!
When the input is [186,419,83,408] 6249, the answer is 26 rather than the correct one 20 .
The coins given by my solution are:
83 83 83 83 83 83 83 83 83 83 83 83 83 186 408 408 408 408 419 419 419 419 419 419 419 419.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        self.ans = float('inf')

        # Start searching from the biggest coin
        coins.sort(reverse=True)
        self.dfs(coins, amount, 0)
        return -1 if self.ans == float('inf') else self.ans

    def dfs(self, coins, amount, prev_count):
        """
        Recursive DFS function to seach valid coins combination.
        First is to use greedy method find out a potential-best solution.
        Then start to search the second biggest coin with pruning when the coins number >= the potential-best solution.

        Args:
            coins: coins list from which we pick coins into combination
            amount: target amount
            prev_count: number of coins picked before this round

        """
        # Set up stop condtion
        if len(coins) == 0:    return

        if amount % coins[0] == 0:
            # Update potential answer
            self.ans = min(self.ans, prev_count + amount // coins[0])
        else:
            for k in range(amount // coins[0], -1, -1):
                # Set up pruning condtion
                if prev_count + k >= self.ans:
                    break
                self.dfs(coins[1:], amount - k * coins[0], prev_count + k)