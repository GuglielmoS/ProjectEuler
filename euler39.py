#!/usr/bin/env python

from math import sqrt
from util import chronometer

@chronometer
def euler39(limit):
	"""
		Condition:
			c^2 = a^2 + b^2
			c^2 = (p - a - b)^2
			c = sqrt(a^2 + b^2)
		So:
			b = p(p - 2a) / 2(p - a)
	"""
	max_perimeter = 0
	max_possibilities = 0
	for cur_p in range(0, limit+1):
		possibilities = []
		for a in range(1, cur_p):
			b = cur_p * (cur_p - 2*a) / (2 * (cur_p - a))
			c = int(sqrt(a**2 + b**2))
			if a + b + c == cur_p:
				candidate = sorted([a,b,c])
				if not candidate in possibilities:
					possibilities.append(candidate)
	
		current_possibilities = len(possibilities)
		if len(possibilities) > max_possibilities:
			max_possibilities = current_possibilities
			max_perimeter = cur_p
			
	return max_perimeter
			
if __name__ == '__main__':
	print euler39(1000)