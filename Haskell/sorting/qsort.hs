{- Quicksort in haskell is very good to appreciate issue.
# blank list is [] [a,b,c] list we say [x:xs] x matches a xs matches [b,c]

-}

qsort1 [] = []
qsort1 (x:xs) = qsort1 small ++ [x] ++ qsort1 big

{- We define what is small and big -}
  where
    small   = [y | y <-  xs, y <= x]
    big  = [y | y <-  xs, y > x]

{- We defined the function how to call this?

#ghci  load program and qsort1[1, 0, -2, -3]) -}
