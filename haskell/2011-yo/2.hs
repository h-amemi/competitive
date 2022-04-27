import Control.Monad
import Data.Text as T

countStr :: String -> String -> Int
countStr pat = T.count (T.pack pat) . T.pack

countStrInRing pat ring = countStr pat (ring ++ Prelude.take (Prelude.length pat - 1) ring)

main = do
  target <- getLine
  ring_count <- readLn :: IO Int
  rings <- replicateM ring_count getLine

  print $ sum [if countStrInRing target ring > 0 then 1 else 0 | ring <- rings]
