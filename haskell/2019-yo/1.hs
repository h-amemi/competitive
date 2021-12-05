toInt :: (String -> Int)
toInt x = read x :: Int

getInts = do
  x <- getLine
  let y = map toInt $words x
  return y

main = do
  x <- getInts

  let a = head x
  let b = x !! 1
  let c = last x

  let coinPerWeek = 7 * a + b
  let week = c `div` coinPerWeek
  let day = ceiling (fromIntegral (c - coinPerWeek * week) / fromIntegral a)

  print $ 7 * week + day
