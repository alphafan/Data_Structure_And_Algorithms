""" Stock buy and sell

The cost of a stock on each day is given in an array, find the max profit
that you can make by buying and selling in those days.

Input:
First line contains number of test cases T. Each test case contain the
integer value 'N' denoting days followed by an array of stock prices in N days.

Output:
The maximum profit is displayed as shown below. And if
there is no profit then print "No Profit".
"""

import sys
import random


def maxProfit(prices, k):
    """ Find maximum profit giving prices within at most k transactions """
    buys, sells = [-sys.maxsize] * k, [-sys.maxsize] * k
    for price in prices:
        for i, (buy, sell) in enumerate(zip(buys, sells)):
            if i == 0:
                buys[i] = max(buy, -price)
                sells[i] = max(sell, buy+price)
            else:
                buys[i] = max(buy, sells[i-1]-price)
                sells[i] = max(sell, buy+price)
    return max(sells)


prices = [random.randint(0, 10) for _ in range(10)]
print(prices)
print(maxProfit(prices, 10))
