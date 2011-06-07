#!/usr/bin/ python
# Using names.txt (http://projecteuler.net/project/names.txt), a 46K text file 
# containing over five-thousand first names, begin by sorting it into 
# alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value 
# by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which 
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?

from util import chronometer

@chronometer
def problem_22():
	file = open('names.txt', 'r')
	names = file.readline().split(',')
	names = [name.replace("\"", "") for name in names]
	names.sort()

	total = 0
	position = 1
	for name in names:
		total += sum([ord(c) - ord('A') + 1 for c in name]) * position
		position += 1
		
	return total

print problem_22()

	

