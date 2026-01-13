#!/usr/bin/python3
import sys

# Function description:
#   Computes the factorial of a non-negative integer n using recursion.
#
# Parameters:
#   n (int): The non-negative integer whose factorial is to be computed.
#
# Returns:
#   int: The factorial of n (n!), i.e., n * (n-1) * ... * 1. By definition, 0! = 1.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)