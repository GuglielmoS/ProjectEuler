#!/usr/bin/python
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

from util import chronometer

def collatz(n):
	length = 0
	while n > 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n + 1
		length += 1
	
	return length

@chronometer
def problem_14():
	max_lenght = 0
	n_max_length = 0 
	for i in range(1, 1000000):
		cur_sequence_length = collatz(i)
		if cur_sequence_length > max_lenght:
			max_lenght = cur_sequence_length
			n_max_length = i

	return n_max_length
	
print problem_14()