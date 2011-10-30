#!/usr/bin/env python

from util import chronometer

@chronometer
def euler31(coins, target):
	ways = [1] + ([0] * target)
	
	for coin in coins:
		for i in range(coin, target+1):
			ways[i] += ways[i-coin]
	
	return ways[target]
	
if __name__ == '__main__':
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	target = 200
	
	print euler31(coins, target)