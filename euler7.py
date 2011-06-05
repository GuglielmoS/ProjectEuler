#!/usr/bin/python
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10001st prime number?

from util import last
from util import primes
from util import chronometer

@chronometer
def problem_7():
	return last(primes(10001))
	
print problem_7()