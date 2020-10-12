class Solution:
    '''
    1. Take one coin at a time.
    2. find the number of ways to make change for target with that one coin and store the result
    3. repeat this, until all the coins are taken (one by one, not all at a time). Update the stored result everytime, by adding the newly found way

    In summary, the number of ways to make change for 5 = sum of number of ways to make change for 5 with each of the coin. (which is dependent on the no.of ways to make 4,3,2,1 etc..
    '''

    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        storage = {}

        def find(target, i):
            if i < 0 or target < 0: return 0

            if (coins[i], target) in storage: return storage[(coins[i], target)]

            if target == 0: return 1

            storage[(coins[i], target)] = find(target - coins[i], i) + find(target, i - 1)
            # print(storage,"with coin",coins[i],"for target",target)
            return storage[(coins[i], target)]

        return find(amount, len(coins) - 1)


'''
{(1, 1): 1} with coin 1 for target 1
{(1, 1): 1, (2, 1): 1} with coin 2 for target 1
{(1, 1): 1, (2, 1): 1, (1, 2): 1} with coin 1 for target 2
{(1, 1): 1, (2, 1): 1, (1, 2): 1, (1, 3): 1} with coin 1 for target 3
{(1, 1): 1, (2, 1): 1, (1, 2): 1, (1, 3): 1, (2, 3): 2} with coin 2 for target 3
{(1, 1): 1, (2, 1): 1, (1, 2): 1, (1, 3): 1, (2, 3): 2, (1, 4): 1} with coin 1 for target 4
{(1, 1): 1, (2, 1): 1, (1, 2): 1, (1, 3): 1, (2, 3): 2, (1, 4): 1, (1, 5): 1} with coin 1 for target 5
{(1, 1): 1, (2, 1): 1, (1, 2): 1, (1, 3): 1, (2, 3): 2, (1, 4): 1, (1, 5): 1, (2, 5): 3} with coin 2 for target 5
{(1, 1): 1, (2, 1): 1, (1, 2): 1, (1, 3): 1, (2, 3): 2, (1, 4): 1, (1, 5): 1, (2, 5): 3, (5, 5): 4} with coin 5 for target 5

'''
#Bottom up
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]