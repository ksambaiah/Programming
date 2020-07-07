removerU :: [c] -> [c]

removeU st = [ c | c->st, c `elem` in ['a'..'z']]
