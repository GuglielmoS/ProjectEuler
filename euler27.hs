factors :: Int -> [Int]
factors n = [x | x <- [1..limit], n `mod` x == 0]
    where limit = n `div` 2

isPrime :: Int -> Bool
isPrime n 
    | factorsNumber == 1 = True
    | otherwise          = False
    where factorsNumber = length $ factors n

sequenceLength :: Int -> Int -> Int
sequenceLength a b = length $ takeWhile isPrime (map euler [1..])
    where euler n = n*n + a*n + b

problem27 = snd $ maximum [(sequenceLength a b, a*b) | a <- [-1000..1000],
                                                       b <- [-999,-997..1000]]

main = do print problem27

