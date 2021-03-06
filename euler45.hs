-- Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
-- 
-- Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
-- Pentagonal	 	Pn=n(3n1)/2	 	1, 5, 12, 22, 35, ...
-- Hexagonal	 	Hn=n(2n1)	 	1, 6, 15, 28, 45, ...
-- It can be verified that T285 = P165 = H143 = 40755.
-- 
-- Find the next triangle number that is also pentagonal and hexagonal.

-- defines the infinite sequences of triangle,pentagonal and hexagonal numbers
ts = scanl (+) 1 [2..]
ps = map (\n -> div (n * (3*n - 1)) 2) [1..]
hs = map (\n -> n * (2*n - 1)) [1..]

-- defines an intersection function used to get the common elements fo two list
-- it works either on infinite list such as ts,ps and hs
intersect :: Ord a => [a] -> [a] -> [a]
intersect [] _ = []
intersect _ [] = []
intersect (x:xs) (y:ys) | x == y    = x : intersect xs ys
                        | x < y     =     intersect xs (y:ys)
                        | otherwise =     intersect (x:xs) ys

-- firstly finds the intersection between the pentagonal and hexagonal numbers
-- then it intersects the result with the triangle numbers and take the third
-- because we know already that the first two are 1 and 40755
p45 = intersect ts candidates !! 2
  where
    candidates = intersect ps hs

-- prints the solution
main = putStrLn $ show p45
