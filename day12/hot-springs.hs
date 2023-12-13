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
        x5 = concat . replicate 5




analyseSpring (record, val) = do
    let reclen = length record
        vallen = length val
        cache = listArray mybounds $ map analyseSpring_idx $ range mybounds
        mybounds = ((0, 0), (reclen, vallen))


        analyseSpring_idx (idx_rec, idx_val) = ret
          where
            ret = aux drecs dvals
            drecs = drop (reclen - idx_rec) record
            dvals = drop (vallen - idx_val) val

    -- let aux' flag record val =
        aux':: Int -> Int -> Int
        aux' idxr idxv =
          -- traceShow (("array index", flag, idxr, idxv, curval)) 
          cache!((idxr, idxv))

          -- let res = aux False record val
          -- in
          -- traceShow res $ res


      -- le booléen indique si on est dans un "intervalle" de #
        aux [] [] = 1
        -- aux False [] [0] = 1
        aux [] [0] = 1 -- error "0 should not appear here"
        aux [] _ = 0
        aux ('.':recs) [] = aux'' recs []
        aux ('?':recs) [] = aux'' recs []
        aux ('#':recs) [] = 0

        aux (c:recs) (0:vals) =
            aux'' (c:recs) (vals)

        aux ('.':recs) (v:vals) = aux'' recs (v:vals)
        aux ('#':recs) (v:vals) =
            aux_in_range recs ((v-1):vals)

        aux ('?':recs) (v:vals) =
            aux'' recs (v:vals) +  -- on fait comme si ? = .
            aux_in_range recs ((v-1):vals) -- on fait comme si ? = #


        aux_in_range _ [] = error "liste des valeurs vides"
        aux_in_range [] [0] = 1
        aux_in_range [] _   = 0
        aux_in_range ('#':recs) (0:_) = 0
        aux_in_range ('#':recs) (v:vals) = aux_in_range recs ((v-1):vals)
        aux_in_range ('.':recs) (0:vals) = aux'' recs vals
        aux_in_range ('.':recs) (v:vals) = 0
        aux_in_range ('?':recs) (0:vals) = aux'' recs vals -- ? = .
        aux_in_range ('?':recs) (v:vals) = aux_in_range recs ((v-1):vals) -- ?= #


        -- aux'' rec [] = aux' (length rec) 0 0
        aux'' recs vals = aux' (length recs) (length vals)

    -- traceShow (cache!(False,0,0)) $
    -- aux' False reclen vallen (head val)
    cache!(reclen, vallen)
