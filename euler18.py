#!/usr/bin/python
# By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below

from util import chronometer

@chronometer
def problem_18():
	triangle = [
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
		[0,0,0,0,0,0,0,0,0,0,0,0,0,95,0,64,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,17,0,47,0,82,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,18,0,35,0,87,0,10,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,20,0,4,0,82,0,47,0,65,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,19,0,1,0,23,0,75,0,3,0,34,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,88,0,2,0,77,0,73,0,7,0,63,0,67,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,99,0,65,0,4,0,28,0,6,0,16,0,70,0,92,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,41,0,41,0,26,0,56,0,83,0,40,0,80,0,70,0,33,0,0,0,0,0,0],
		[0,0,0,0,0,41,0,48,0,72,0,33,0,47,0,32,0,37,0,16,0,94,0,29,0,0,0,0,0],
		[0,0,0,0,53,0,71,0,44,0,65,0,25,0,43,0,91,0,52,0,97,0,51,0,14,0,0,0],
		[0,0,0,70,0,11,0,33,0,28,0,77,0,73,0,17,0,78,0,39,0,68,0,17,57,0,0,0],
		[0,0,91,0,71,0,52,0,38,0,17,0,14,0,91,0,43,0,58,0,50,0,27,0,29,0,48,0,0],
		[0,63,0,66,0,4,0,68,0,89,0,53,0,67,0,30,0,73,0,16,0,69,0,87,0,40,0,31,0],
		[4,0,62,0,98,0,27,0,23,0,9,0,70,0,98,0,73,0,93,0,38,0,53,0,60,0,4,0,23]]

	def explore(triangle, total_sum, next_x, next_y):
		if next_x < 0 or next_x >= len(triangle):
			return total_sum
		
		if next_y < 0 or next_y >= len(triangle[next_x]):
			return total_sum

		if triangle[next_x][next_y] != 0:
			left_path = explore(triangle, total_sum + triangle[next_x][next_y], next_x+1, next_y-1) 
			right_path = explore(triangle, total_sum + triangle[next_x][next_y], next_x+1, next_y+1)

			if left_path > right_path:
				return left_path
			else:
				return right_path
		else:
			return 0
	
	return explore(triangle, 0, 0, 14)
	
print problem_18()