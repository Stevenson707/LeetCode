def maxProfit(prices):

    # Run time: 0 ms
    max_profit = 0
    min_price = float("inf")
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

    # Run time: 133 ms
    # maxP = 0
    # minBuy = prices[0]
    # for sell in prices:
    #     maxP = max(maxP, sell - minBuy)
    #     minBuy = min(minBuy, sell)
    # return maxP

    # Memory Limit exceeded (my solution)
    # results = []
    # if len(prices) < 2:
    #     return 0
    # for i in range(len(prices)):
    #     for j in range(i + 1, len(prices)):
    #         results.append(prices[j] - prices[i])
    # if max(results) < 0:
    #     return 0
    # return max(results)


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
