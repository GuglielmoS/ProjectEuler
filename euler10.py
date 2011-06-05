#!/usr/bin/python
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from util import is_prime
from util import chronometer

@chronometer
def problem_10():
	return sum([n for n in range(3, 2000000, 2) if is_prime(n)])

print problem_10()