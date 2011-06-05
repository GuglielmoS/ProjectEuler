#!/usr/bin/python
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers 
# is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from util import chronometer
from util import is_palindrome

@chronometer
def problem_4():
	largest_product = 0
	for i in range(100, 999):
		for j in range(100, 999):
			product = i*j
			if is_palindrome(product):
				if product > largest_product:
					largest_product = product
	return largest_product
	
print problem_4()