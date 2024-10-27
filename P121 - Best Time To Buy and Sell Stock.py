def maxProfit(prices):
    max_profit = 0
    current_day = 0
    next_day = 1
    while next_day < len(prices):
        profit = prices[next_day] - prices[current_day]
        if prices[current_day] < prices[next_day]:
            max_profit = max(profit, max_profit)
        else:
            current_day = next_day
        next_day += 1
    return max_profit


lst = []
print(maxProfit(lst))
