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

    -- let dat2 = map duplicSpring dat
--
    -- print $ dat2
--
    -- print $ sum $ map analyseSpring dat2



duplicSpring (record, val) = (recx5, valx5)
  where _:recx5 = x5 ('?':record)
        valx5 = x5 val
        x5 l = concat $ replicate 5 l




analyseSpring (record, val) = do
    let reclen = length record
        vallen = length val
        valmax = maximum val
        cache = listArray mybounds $ map analyseSpring_idx $ range mybounds
        mybounds = ((False, 0, 0, 0), (True,reclen, vallen, valmax))


        analyseSpring_idx (flag, idx_rec, idx_val, cur_val) = traceShow (("springidx", flag, idx_rec, idx_val, ret)) $ ret
          where
            ret = aux flag (drop (reclen - idx_rec) record)
                           values
            values = 
              if cur_val == 0 
                then (drop (vallen - idx_val) val)
                else (cur_val:(drop (vallen - idx_val+1) val))


    -- let aux' flag record val =
        aux':: Bool -> Int -> Int -> Int -> Int
        aux' flag idxr idxv curval =
          traceShow (("array index", flag, idxr, idxv, curval)) $ cache!((flag, idxr, idxv, curval))

          -- let res = aux False record val
          -- in
          -- traceShow res $ res


      -- le booléen indique si on est dans un "intervalle" de #
        aux False [] [] = traceShow "COUCOU FINI" $ 1
        -- aux False [] [0] = 1
        aux False [] [0] = 1 -- error "0 should not appear here"
        aux False [] _ = 0
        aux False ('.':recs) [] = aux'' False recs []
        aux False ('?':recs) [] = aux'' False recs []
        aux False ('#':recs) [] = 0

        aux False (c:recs) (0:vals) =
            aux'' False (c:recs) (vals)

        aux False ('.':recs) (v:vals) = aux'' False recs (v:vals)
        aux False ('#':recs) (v:vals) =
            aux'' True recs ((v-1):vals)

        aux False ('?':recs) (v:vals) =
            aux'' False recs (v:vals) +  -- on fait comme si ? = .
            aux'' True recs ((v-1):vals) -- on fait comme si ? = #


        aux True _ [] = error "liste des valeurs vides"
        aux True [] [0] = 1
        aux True [] _   = 0
        aux True ('#':recs) (0:_) = 0
        aux True ('#':recs) (v:vals) = aux'' True recs ((v-1):vals)
        aux True ('.':recs) (0:vals) = aux'' False recs vals
        aux True ('.':recs) (v:vals) = 0
        aux True ('?':recs) (0:vals) = aux'' False recs vals -- ? = .
        aux True ('?':recs) (v:vals) = aux'' True recs ((v-1):vals) -- ?= #


        aux'' flag rec [] = aux' flag (length rec) 0 0
        aux'' flag rec (curv:vals) = aux' flag (length rec) (length (curv:vals)) curv

    -- traceShow (cache!(False,0,0)) $
    aux' False reclen vallen (head val)
