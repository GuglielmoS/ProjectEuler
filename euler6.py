#!/usr/bin/python
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

from util import square
from util import chronometer

@chronometer
def problem_6(max):
	natural_numbers = range(1, max+1)
	return square(sum(natural_numbers)) - sum(map(square, natural_numbers))
	
print problem_6(100)