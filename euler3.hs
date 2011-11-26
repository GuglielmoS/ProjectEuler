isPrime :: Int -> Bool
isPrime n | factorsNumber == 1 = True
		  | otherwise = False
		where
			factorsNumber = length $ factors n

factors :: Int -> [Int]
factors n = [x | x <- [1..limit], n `mod` x == 0]
	where
		limit = floor $ sqrt (fromIntegral n) 

primeFactors :: Int -> [Int]
primeFactors n = filter isPrime (factors n)

problem3 = last (primeFactors 600851475143)

main = do print problem3
