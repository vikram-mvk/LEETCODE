'''
Top down approach with DP
https://leetcode.com/media/original_images/322_coin_change_tree.png
https://leetcode.com/problems/coin-change/solution/

'''
def coinChange(self, coins: List[int], amount: int) -> int:
    if amount < 1: return 0

    dp = [-1] * (amount + 1)

    def find(current_amt):
        if current_amt == 0: return 0  # return 0 and the back track will add +1  and send it to its caller and so on until original caller
        if current_amt < 0: return float('inf')  # return inf. inf + 1 is inf. So on backtrack it will return inf

        if dp[current_amt] != -1: return dp[current_amt]  # if it is not -1, it has been explored. so return

        min_ways = float('inf')
        for c in coins:
            res = find(current_amt - c) + 1
            min_ways = min(min_ways, res)
        dp[current_amt] = min_ways
        return dp[current_amt]

    find(amount)

    return dp[-1] if dp[-1] != float('inf') else -1

#same solution using dict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1: return 0

        dp = {}

        def find(current_amt):
            if current_amt == 0: return 0  # return 0 and the back track will add +1  and send it to its caller and so on until original caller
            if current_amt < 0: return float('inf')  # return inf. inf + 1 is inf. So on backtrack it will return inf

            if current_amt in dp: return dp[current_amt]  # if it is not -1, it has been explored. so return

            min_ways = float('inf')

            for c in coins:  min_ways = min(min_ways, find(current_amt - c) + 1)

            dp[current_amt] = min_ways  # store the computed result in dp

            return min_ways

        find(amount)

        return dp[amount] if dp[amount] != float('inf') else -1

#Bottom up approach
class Solution:
    '''
    The min ways to make amount=11 is based on the min ways to make amounts 0 to 10
    bottom up approach:
    1. Use the coin 1 first. and fill the dp [i.e., finding the min number of ways to go to amount with coin 1]
    2. Now include coin 2 and check if it reduces the number of ways to get to the amount
    3. repeat 2, for all coins in array
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<1: return 0
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1


#BFS approach
class Solution:
    def coinChange(self, coins, amount):
        visited = set()
        queue = deque([(amount, 0)])  # (remainder, coin_count)
        coins.sort(reverse=True)

        while queue:  # bfs / shortest path
            remainder, coin_count = queue.popleft()
            if remainder not in visited:
                if remainder == 0:
                    return coin_count
                if remainder < 0:
                    continue

                for coin in coins:
                    queue.append((remainder - coin, coin_count + 1))

                visited.add(remainder)

        return -1