#!/usr/bin/python
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

from util import digits_sum
from util import chronometer

@chronometer
def problem_16():
	return digits_sum(2**1000)
	
print problem_16()