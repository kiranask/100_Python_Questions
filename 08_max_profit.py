"""
SDET / DevOps Interview | Coding Round | Code 12
Question: You are given an array prices where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#pythonprogramming #pythoncode #pythoninterview #testing #softwaretesting

How to remember

profit = stocks[i] - min

max_profit = max(profit, max_profit)

"""
def max_profit(stocks):
    max_profit =0
    min = float('inf')

    for i in range( len(stocks)):
        if stocks[i]< min:
            min= stocks[i]

        profit = stocks[i] - min
        if profit > max_profit:
            max_profit= profit
    return max_profit


print(max_profit([9,2,3,2,1,9]))