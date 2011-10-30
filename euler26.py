#!/usr/bin/python

import operator

from util import chronometer

@chronometer
def euler26(limit):
	"""
		http://en.wikipedia.org/wiki/Repeating_decimal
		
		condition:
			a^m = 1 (mod n)		
		
		where:
			1. a is coprime to n
			2. m is the length of the recurrying cycle 
			   of 1/n
	"""
	candidates = {}
	
	for n in range(2, limit+1):
		for k in range(1, n):
			if (10 ** k) % n == 1:
				candidates[n] = k
				break
		
	return max(candidates.iteritems(), key=operator.itemgetter(1))
	
if __name__ == '__main__':
	print euler26(1000)