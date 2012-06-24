#!/usr/bin/python
#
# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:
#
#    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
#    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
#    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)
#
# As 1 = 1^(4) is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

from util import digits
from util import chronometer

def sum_digits_at_fifth_power(n):
    """
        Returns the sum of the fifth power of each
        digit of the number 'n'.
    """
    return sum(map(lambda x: x**5, digits(n))) 

def is_valid(n):
    return n == sum_digits_at_fifth_power(n)

def get_max_value():
    return 5 * 9**5

@chronometer
def problem_30():
    return sum(filter(is_valid, range(2, get_max_value())))

print problem_30()
