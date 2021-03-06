#!/usr/bin/python

import time
import operator
import itertools

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
	
	limit = int(sqrt(n))+1
	for i in range(3, limit, 2):
		if n % i == 0:
			return False
			
	return True
	
def primes(n):
	""" Returns a list that contains the first n prime numbers.
	"""
	
	i = 3
	primes = [2]
	while len(primes) < n:
		if is_prime(i):
			primes.append(i)
		i += 2

	return primes		
	
def primes_below(limit):
	""" Return all the primes number below limit. """ 
	all_primes = [2]
	
	for n in range(3, limit, 2):
		if is_prime(n):
			all_primes.append(n)
			
	return all_primes
	
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

def factorize(n):
	""" Returns a list that contains all factors
	    of the number n.
	"""
	factors = []
	limit = int(ceil((n / 2) + 1))
	for i in range(1, limit):
		if n % i == 0:
			factors.append(i)
	
	return factors

def count_factors(n):
	""" Returns the number of factors of the number n """
	
	if (n == 1):
		return 1
	
	count = 0
	limit = int(n ** 0.5) + 1
	for i in range(1, limit):
		if n % i == 0:
			count += 2			
		
	return count
			
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
	
def square(n):
	""" Returns the square of the number n.
	"""
	return n*n
	
def last(vector):
	""" Returns the last element of a list.
	"""
	return vector[-1]
	
def factorial(n):
	""" Return the factorial of the number n """
	return reduce(operator.mul, range(1, n+1))

def digits_sum(n):
	""" Returns the sum of all the digits of the number n """
	return sum(map(int, list(str(n))))
	
def is_amicable(n):
	""" Returns True if n is an amicable number, False otherwise. """
	factors_sum = sum(factorize(n))	
	if n != factors_sum and n == sum(factorize(factors_sum)):
		return True

	return False
	
def fibonacci_generator():
	""" It is a generator of the fibonacci sequence. """
	n1, n2 = 0, 1
	while True:
		yield n1
		n1, n2 = n2, n1 + n2
		
def is_abundant(n):
	""" Return true if n is an abundant number, false otherwise """
	return sum(factorize(n)) > n
	
def combinations(iterable):
	""" Return a list containing all the combinations of iterable element."""
	combinations_list = []
	for i in range(1, len(iterable)+1):
		combinations_list.append(list(itertools.combinations(iterable, i)))
	
	return combinations_list
	
def combinations_with_replacement(iterable):
	""" Return a list containing all the combinations with replacement 
		of iterable element."""
	combinations_list = []
	for i in range(1, len(iterable)+1):
		combinations_list.append(list(itertools.combinations_with_replacement(iterable, i)))
	
	return combinations_list
	
def simplify_fraction(f):
    """ 
        Assuming that f is a fraction, it returns the simplified version.
        So f should be a tuple of two elements, in which the first is
        the numerator and the second is the denominator.
    """
    f_gcd = gcd(f[0], f[1])
    
    return (f[0]/f_gcd, f[1]/f_gcd)    

def digits(n):
    """
        Returns a list that contains all the digits of the number 'n'.
    """
    return map(int, str(n))

