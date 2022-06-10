egcd a b 
     | a < b = egcd b a
     | b == 0 = a
     | otherwise = egcd b (a `mod` b)

