#!/usr/bin/python3
"""
Function that calculates the minimum operations to achieve
exactly n 'H' characters in a file, using only Copy All and Paste operations
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of characters

    Returns:
        int: Minimum number of operations, or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
