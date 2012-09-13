import Data.Char

fact :: Int -> Int 
fact n = foldl (*) 1 [2..n] 

digits :: Int -> [Int]
digits n = map digitToInt (show n)

sumDigitsFact :: Int -> Int
sumDigitsFact n = sum $ map fact (digits n)

problem34 = sum $ filter (\x -> x == sumDigitsFact x) [3..9999999] 

main = do print problem34
