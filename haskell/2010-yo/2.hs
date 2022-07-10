import Control.Monad

toInt :: (String -> Int)
toInt x = read x :: Int

getInts = do
  x <- getLine
  let y = map toInt $words x
  return y

susumeru :: [Int] -> [Int] -> Int -> Int -> Int
susumeru [] [] 0 0 = 0
susumeru sugoroku (dice : dices) zahyo kaisu =
  if zahyo + dice + (sugoroku !! zahyo + dice) >= length sugoroku
    then kaisu + 1
    else susumeru sugoroku dices (zahyo + dice + (sugoroku !! zahyo + dice)) (kaisu + 1)

main = do
  [n, m] <- getInts

  sugoroku <- replicateM n readLn
  dices <- replicateM m readLn
  print $ susumeru sugoroku dices 0 0
