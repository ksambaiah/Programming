bubbleSort :: Ord a => [a] -> [a]
bubbleSort = foldr swapTill []

swapTill x [] = [x]
swapTill x (y:xs) = min x y : swapTill (max x y) xs
