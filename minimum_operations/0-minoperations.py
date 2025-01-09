#!/usr/bin/python3
def minOperations(n):
    """
    Calculate the minimum number of operations to get exactly n 'H' characters.

    Parameters:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations or 0 if n is impossible.
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
