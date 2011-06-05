#!/usr/bin/python

import time
from math import sqrt
from math import ceil

def chronometer(function):
	""" It's a decorator used to know the execution's time
	    of the decorated function.
	"""
	
	def decorated_function(*args, **kwargs):
		start_time = time.time()
		returned_value = function(*args, **kwargs)
		print "[@] %s executed in %.4f seconds" % (function.func_name, 
												   time.time() - start_time)
		return returned_value
	return decorated_function

def memoize(function):
	""" It's a decorator that allows to store previous results of
	    the decorated function.
	"""
	
	cache = {}
	def decorated_function(*args):
		try:
			return cache[args]
		except KeyError:
			returned_value = function(*args)
			cache[args] = returned_value
			return returned_value
	return decorated_function
	
def is_prime(n):
	""" Checks if the number n is prime.
	    Return True in case of success, False otherwhise
    """
	
	if n <= 3:
		return True
	
	limit = int(sqrt(n))
	for i in range(3, limit, 2):
		if n % i == 0:
			return False
			
	return True
	
def factorize(n):
	""" Returns a list that contains all factors
	    of the number n.
		The number is prime when the list contains only the number self.
	"""
	factors = []
	limit = int(sqrt(n))
	for i in range(2, limit+1):
		if n % i == 0:
			factors.append(i)
			n /= i
	
	if len(factors) == 0:
		factors.append(n)
	
	return factors
	
def prime_factors(n):
	""" Returns a list that contains all the prime factors of
	    the number n.
	"""
	
	p_factors = []
	limit = int(sqrt(n))
	for i in range(3, limit, 2):
		if n % i == 0 and is_prime(i):
			p_factors.append(i)
	
	return p_factors
			
def is_palindrome(n):
	""" Returns True if the number n is palindrome, False otherwise
	"""
	n_str = str(n)
	return n_str == n_str[::-1]
	
def gcd(a, b):
	""" Returns the greatest common divisor of a and b.
	"""
	while b:
		a, b = b, a % b
	return a
	
def lcm(a, b):
	""" Returns the least common multiple of a and b.
	"""
	return a * b // gcd(a, b)
	
	
	
	
	
	