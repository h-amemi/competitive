toInt :: (String -> Int)
toInt x = read x :: Int

getInts = do
  x <- getLine
  let y = map toInt $words x
  return y

getInt = do
  x <- getLine
  let y = toInt x
  return y

mapInd :: (a -> Int -> b) -> [a] -> [b]
mapInd f l = zipWith f l [0 ..]

-- susumu :: [Int] -> [Int] -> [Int]
-- susumu [] [] = []
-- susumu sugoroku (deme : tl) = sugoroku !! deme + 1 : (sugoroku !! deme + 1) + 1

-- susumu sogoroku tl

susumeru 0 action = return ()
susumeru n action = do
  action

  susumeru (n - 1) action

main = do
  n <- getInt
  print n
  x <- getInts
  print x
  m <- getInt
  print m
  a <- getInts
  print a

  mapInd (x !! a + 1 : 1 + a) a
  print x
