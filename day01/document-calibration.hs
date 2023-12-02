{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE QuasiQuotes #-}

import AoC
import Control.Applicative
import Control.Exception
import Control.Monad
import Control.Monad.ST
import qualified Data.Algebra.Boolean as B
import Data.Char
import Data.List
import Data.Maybe
import Data.Function
import Data.Array
import Data.Array.ST
import Data.Tuple.Extra
import Data.Graph

import GHC.Utils.Misc

import Debug.Trace
import qualified Data.Text as T
import qualified Data.Sequence as S
import Text.ParserCombinators.ReadP hiding (count)
import Text.Printf
-- import Text.Scanf



-- If part1 and part2 are very different,
-- toggle which part to compute with this flag.
part2 = True

main :: IO ()
main = do
    lignes <- getContents >>= pure . lines

    print lignes
    let result = foldl addAnalyseLine 0 lignes

    print result

addAnalyseLine acc l = traceShow lconv $
    acc + chercheDigits lconv
  where
    chercheDigits l = 10*(head l) + last l
    lconv = conv l
    conv [] = []
    conv ('o':'n':'e':cs)         = 1 : conv ('e':cs)
    conv ('t':'w':'o':cs)         = 2 : conv ('o':cs)
    conv ('t':'h':'r':'e':'e':cs) = 3 : conv ('e':cs)
    conv ('f':'o':'u':'r':cs)     = 4 : conv cs
    conv ('f':'i':'v':'e':cs)     = 5 : conv ('e':cs)
    conv ('s':'i':'x':cs)         = 6 : conv cs
    conv ('s':'e':'v':'e':'n':cs) = 7 : conv cs
    conv ('e':'i':'g':'h':'t':cs) = 8 : conv ('t':cs)
    conv ('n':'i':'n':'e':cs)     = 9 : conv ('e':cs)
    conv (c:cs)
      | isDigit c = chrDigit c : conv cs 
      | otherwise = conv cs

