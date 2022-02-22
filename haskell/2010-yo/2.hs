import Control.Monad

toInt :: (String -> Int)
toInt x = read x :: Int

getInts = do
  x <- getLine
  let y = map toInt $words x
  return y

susumeru :: [Int] -> [Int] -> Int -> Int -> Int
susumeru [] [] 0 0 = 0 # sugoroku saikoro zahyo kaisu
susumeru xs (y : ys) z a = if z + (xs !! z + y) >= length sugoroku then a + 1 else susumeru xs ys z + (xs !! z + y) a + 1

main = do
  [n, m] <- getInts

  sugoroku <- replicateM n readLn
  saikoro <- replicateM m readLn
  print $ susumeru sugoroku saikoro 0 0
