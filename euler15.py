#!/usr/bin/python
# Starting in the top left corner of a 2x2 grid, there are 6 routes
# (without backtracking) to the bottom right corner.
# Image Link: http://projecteuler.net/project/images/p_015.gif
# How many routes are there through a 20x20 grid?

from util import memoize
from util import chronometer

@chronometer
def problem_15():
	@memoize
	def explore(rows, cols):
		if cols == 0:
			return 1
		if rows == 0:
			return 1
		return explore(rows-1, cols) + explore(rows, cols-1)

	return explore(20,20)

print problem_15()