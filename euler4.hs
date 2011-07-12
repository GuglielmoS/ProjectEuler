isPalindrome :: Int -> Bool
isPalindrome n | nStr == nReversedStr = True
 			   | otherwise = False
			where
				nStr = show n
				nReversedStr = reverse nStr

problem4 = maximum $ palindromeProducts 
	where
		products = [x*y | x <- [100..999], y <- [x..999]]
		palindromeProducts = filter isPalindrome products
