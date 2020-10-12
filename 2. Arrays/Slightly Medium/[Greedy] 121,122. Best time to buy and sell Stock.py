#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    curr_profit = 0
    # initially we assume that stock is cheapest on first day. so buy it
    buying_price = prices[0]
    # we're not gonna but at day 0 and sell at day 0. so start with i=1
    i = 1

    while i < len(prices):
        # if stock is cheaper today, buy it today
        if prices[i] < buying_price:
            buying_price = prices[i]

        # if buying_price is updated at i, we dont need to check. otherwise we check if today's price - buying_price is greater than curr profit
        elif prices[i] - buying_price > curr_profit:
            curr_profit = prices[i] - buying_price
        i += 1

    return curr_profit
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#QN:2
def maxProfit(self, prices: List[int]) -> int:
    i = 0
    profit = 0
    while i < len(prices) - 1:
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]

        i += 1
    return profit