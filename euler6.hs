problem6 =  squareOfSum - sumOfSquares
	where 
		sumOfSquares = sum [x^2 | x <- [1..100]]
		squareOfSum = (sum [1..100]) ^ 2