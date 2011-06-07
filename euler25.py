#!/usr/bin/python
# The Fibonacci sequence is defined by the recurrence relation:
#    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

from util import chronometer
from util import fibonacci_generator

@chronometer
def problem_25():
	n = 0
	fib = fibonacci_generator()
	while True:
		cur_term = fib.next()
		if len(str(cur_term)) >= 1000:
			return n
		n += 1

print problem_25()