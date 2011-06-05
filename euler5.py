#!/usr/bin/python
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

from util import lcm
from util import gcd
from util import chronometer

@chronometer
def problem_5():
	n = 0     # because the problem says that 2520 is the smallest 
				 # with the numbers from 1 to 10 as divisors.
	while True:
		n += 20
		divs = 2
		while n % divs == 0 and divs <= 20:
			divs += 1
		if divs == 21:
			return n

@chronometer
def problem_5_fast():
	return reduce(lcm, range(1, 20))

# print problem_5() # it is slow
print problem_5_fast()