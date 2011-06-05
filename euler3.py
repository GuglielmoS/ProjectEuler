#!/usr/bin/python
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from util import chronometer
from util import prime_factors

@chronometer
def problem_3(n):
	return max(prime_factors(n))
	
print problem_3(600851475143)