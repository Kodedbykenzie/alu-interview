#!/usr/bin/python3
"""
This module contains a function `minOperations` that calculates the minimum
number of operations required to get exactly `n` 'H' characters using
'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get exactly n 'H' characters.

    Parameters:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations or 0 if n is impossible or invalid.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
