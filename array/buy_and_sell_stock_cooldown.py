""" Buy and Sell Stocks with Cool Down """

import sys
import random


def maxProfit(prices):
    buys = [-sys.maxsize] * len(prices)
    sells = [0] * len(prices)
    buys[0] = -prices[0]
    buys[1] = max(-prices[0], -prices[1])
    sells[1] = max(0, buys[1]+prices[1])
    for i in range(2, len(prices)):
        buys[i] = max(buys[i-1], sells[i-2]-prices[i])
        sells[i] = max(sells[i-1], buys[i-1]+prices[i])
    for p, b, s in zip(prices, buys, sells):
        print(p, '\t', b, '\t', s)


test = [random.randint(0, 10) for _ in range(10)]
maxProfit(test)
