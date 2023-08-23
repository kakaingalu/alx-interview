#!/usr/bin/python3
"""generates change
"""


def makeChange(coins, total):
    """A function that determines the
    fewest number of coins needed to
    meet a given amount total
    Args:
        coins (_type_): a list of the values
        of the coins in your possession
        total (_type_): total amount
    return:
           fewest number of coins needed
           to meet total
    """
    memo = {}  # Dictionary for memoization
    
    def minCoins(amount):
        if amount in memo:
            return memo[amount]
        
        if amount == 0:
            return 0
        
        min_count = float('inf')
        
        for coin in coins:
            if coin <= amount:
                count = 1 + minCoins(amount - coin)
                min_count = min(min_count, count)
        
        memo[amount] = min_count
        return min_count
    
    result = minCoins(total)
    
    if result == float('inf'):
        return -1
    else:
        return result
