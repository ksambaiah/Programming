qsort1 [] = []
qsort1 (x:xs) = qsort1 small ++ [x] ++ qsort1 big
    where
        small = [y | y <- xs, y <= x]
        big   = [y | y <- xs, y > x]
