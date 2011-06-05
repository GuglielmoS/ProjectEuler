#!/usr/bin/python
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from util import chronometer

@chronometer
def problem_1(max):
	return sum([n for n in range(0, max) if n % 3 == 0 or n % 5 == 0])

print problem_1(1000)