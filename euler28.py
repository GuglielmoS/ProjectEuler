#!/usr/bin/bin python
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?

from util import chronometer

@chronometer
def problem_28():
	step = 2
	current = 3
	total_sum = 1
	limit = 1001/2
	for i in range(0, limit):
		total_sum += current * 4 + step * 6
		current += step * 3
		step += 2
		current += step

	return total_sum

print problem_28()