#!/usr/bin/env python

from util import factorize
from util import chronometer

def is_abundant(n):
	return sum(factorize(n)) > n
	
def get_all_abundants_below(limit):
	abundants = []

	for n in range(1, limit):
		if is_abundant(n):
			abundants.append(n)
			
	return abundants

@chronometer
def solve(limit):
	result_list = range(limit)
	all_abundants = get_all_abundants_below(limit) 
	
	for x in all_abundants:
		for y in all_abundants:
			if x + y >= limit:
				break
				
			result_list[x + y] = 0
	
	return sum(result_list)
	
if __name__ == '__main__':
	print solve(28123)
