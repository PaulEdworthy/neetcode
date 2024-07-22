from typing import List


def max_profit(prices: List[int]):
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    print(max_profit)
    return max_profit


a = [7, 1, 5, 3, 6, 4]  # 5
b = [7, 6, 4, 3, 1]  # 0
max_profit(a)
max_profit(b)
