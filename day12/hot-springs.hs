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
part2 = False

parseInput = parseSpring `sepBy1` lineReturn

parseSpring = do
    r <- springRecord 
    skipSpaces
    v <- numberList
    return (r, v)

springRecord = munch1 (\e -> e `elem` ".#?")

main :: IO ()
main = do
    dat <- parseContents parseInput

    print dat
    print $ sum $ map analyseSpring dat

    let dat2 = map duplicSpring dat

    print $ dat2

    print $ sum $ map analyseSpring dat2



duplicSpring (record, val) = (recx5, valx5)
  where _:recx5 = x5 ('?':record)
        valx5 = x5 val
        x5 l = concat $ replicate 5 l





analyseSpring (record, val) =
    let res = aux False record val
    in
    traceShow res $ res


-- le booléen indique si on est dans un "intervalle" de #
aux False [] [] = 1
-- aux False [] [0] = 1
aux False [] [0] = error "0 should not appear here"
aux False [] _ = 0
aux False ('.':recs) [] = aux False recs []
aux False ('?':recs) [] = aux False recs []
aux False ('#':recs) [] = 0

aux False ('.':recs) (v:vals) = aux False recs (v:vals)
aux False ('#':recs) (v:vals) = aux True recs ((v-1):vals)
aux False ('?':recs) (v:vals) =
    aux False recs (v:vals) +  -- on fait comme si ? = .
    aux True recs ((v-1):vals) -- on fait comme si ? = #


aux True _ [] = error "liste des valeurs vides"
aux True [] [0] = 1
aux True [] _   = 0
aux True ('#':recs) (0:_) = 0
aux True ('#':recs) (v:vals) = aux True recs ((v-1):vals)
aux True ('.':recs) (0:vals) = aux False recs vals
aux True ('.':recs) (v:vals) = 0
aux True ('?':recs) (0:vals) = aux False recs vals -- ? = .
aux True ('?':recs) (v:vals) = aux True recs ((v-1):vals) -- ?= #



