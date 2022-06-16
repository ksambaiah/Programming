min [x] = x
min (x:y:xs)  
         | x > y = min (y:xs)
         | otherwise = min (x:xs)

