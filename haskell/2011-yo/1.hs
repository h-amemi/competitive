import Control.Monad

main = do
  secs <- replicateM 4 readLn

  print $ sum secs `div` 60
  print $ sum secs `mod` 60
