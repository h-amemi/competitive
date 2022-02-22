import Control.Monad

main = do
  goukei <- readLn
  prices <- replicateM 9 readLn

  print $ goukei - sum prices
