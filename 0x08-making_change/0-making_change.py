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
    if total == 0 or total < 0:
        return 0
    arr = [float('inf')] * (total + 1)
    arr[0] = 0

    for k in range(1, total + 1):
        for coin in coins:
            if coin <= k:
                arr[k] = min(arr[k], 1 + arr[k - coin])

    if arr[total] == float('inf'):
        return -1
    else:
        return arr[total]
