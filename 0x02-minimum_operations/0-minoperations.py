#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations \
        needed to achieve exactly n 'H' characters in the file.

    Arguments:
    - n: An integer representing the desired number of 'H' characters.

    Returns:
    - An integer representing the minimum number of operations needed.

    If it is impossible to achieve the desired number\
        of 'H' characters, the function returns 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
