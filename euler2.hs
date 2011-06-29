fibonacci_terms = 1 : 1 : zipWith (+) fibonacci_terms (tail fibonacci_terms)
problem_2 =	sum $ [n | n <- takeWhile (<= 4000000) fibonacci_terms, even n]
