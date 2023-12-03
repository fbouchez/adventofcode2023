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


data Color = Red | Green | Blue deriving(Show, Eq)


strCol "green" = Green
strCol "red" = Red
strCol "blue" = Blue

parseInput = do
    games <- sepBy1 parseGame lineReturn
    skipSpaces
    eof
    return games

parseGame = do
    string "Game "
    id <- number
    colonSep
    sets <- sepBy1 parseSets semicolSep

    return (id, sets)

parseSets = sepBy1 parseColor commaSep

parseColor = do
    num <- number
    skipSpaces
    w <- word
    return (num, strCol w)

main :: IO ()
main = do
    dat <- parseContents parseInput
    print dat

    let result = part1 dat
    putStrLn $ "Résultat partie1 : " ++ show result

    let result2 = part2 dat
    putStrLn $ "Résultat partie2 : " ++ show result2


part1 games = foldl addIfValid 0 games
  where
    addIfValid acc (ident, sets) =
      acc + if validSets sets then ident else 0

    validSets sets = foldl accCheckSet True sets
    accCheckSet flag set = foldl accCheckColor flag set

    accCheckColor flag (num, col) = flag && checkCol col num

    checkCol Red n   = n <= 12
    checkCol Green n = n <= 13
    checkCol Blue n  = n <= 14



part2 games = foldl addPower 0 games
  where
    addPower pow (_, sets) = pow + power sets

    power sets = maxr * maxg * maxb
      where
        (maxr, maxg, maxb) = computeMaxCol sets
        computeMaxCol sets = 
          foldl accMaxCurrentSet  (0, 0, 0) sets

        accMaxCurrentSet themax [] = themax
        accMaxCurrentSet themax ((ncol, col):colors) =
          accMaxCurrentSet (update themax col ncol) colors

        update (mr, mg, mb) Red r = (max mr r, mg, mb)
        update (mr, mg, mb) Green g = (mr, max mg g, mb)
        update (mr, mg, mb) Blue b = (mr, mg, max mb b)


