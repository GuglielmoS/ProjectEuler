fibonacci = 0 : 1 : zipWith (+) fibonacci (tail fibonacci)
euler_2 = sum (filter even (takeWhile (<4000000) fibonacci))
main = do print euler_2
