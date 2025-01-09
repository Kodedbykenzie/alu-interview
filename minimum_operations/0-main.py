#!/usr/bin/python3
"""
Main file for testing the `minOperations` function.
"""

minOperations = __import__('0-minoperations').minOperations

# Test cases
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 21
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = -12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
