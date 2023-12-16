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


data Initseq = Minus String | Equal String Int deriving (Show)


parsePart1 = (munch1 ((/=) ',')) `sepBy1` commaSep

parsePart2 = parseInitSeq `sepBy1` commaSep


parseInitSeq = do
    w <- word
    mayb <- parseRest
    case mayb of
      Nothing -> return $ Minus w
      Just i  -> return $ Equal w i

parseRest = do
    (char '=' >> number >>= return . Just) <|> (char '-' >> return Nothing)






main :: IO ()
main = do
    contents <- getContents

    dat1 <- applyParser parsePart1 contents
    dat2 <- applyParser parsePart2 contents
    print dat1
    print dat2

    print $ "HASH" ++ show (hash "HASH")


    let boxes = applyInitSequence dat2

    putStr "Boites partie 2 : "
    print $ boxes

    let res2 = calculFinal boxes

    putStr "Résultat partie 1 : "
    print $ sum $ map hash dat1
    putStr "Résultat partie 2 : "
    print $ res2




hash = hash' 0


hash' cur [] = cur
hash' cur (c:cs) = hash' new_cur cs
  where
    new_cur = ((cur + asciicode) * 17) `mod` 256
    asciicode = ord c




applyInitSequence :: [Initseq] -> Array Int [(String, Int)]
applyInitSequence initlist = accumArray accFunc [] (0,255) seqlist
  where
    seqlist = traceShowId $ map computeAssoc initlist
    computeAssoc (Minus lbl) = (hash lbl, Minus lbl)
    computeAssoc (Equal lbl foc) = (hash lbl, Equal lbl foc)

    accFunc :: [(String, Int)] -> Initseq -> [(String, Int)]
    accFunc old (Minus lbl) = filter (((/=) lbl) . fst) old

    accFunc [] (Equal lbl foc) = [(lbl, foc)]
    accFunc ((l,f):lenses) init@(Equal lbl foc)
      | l == lbl  = (l, foc):lenses
      | otherwise = (l,f) : accFunc lenses init

   
-- do
    -- let boxes = listArray (0,255) [ [] | _ <- [0..255]] :: Array Int [Int]
--
    -- aux boxes initlist



-- aux boxes [] = calculFinal boxes
-- aux boxes (seq:seqs) = aux boxes' seqs
  -- where
    -- boxes' = applySequence boxes
--

calculFinal = sum . map (snd . compute1box) . assocs

compute1box (box_idx, box) = foldl accu (1, 0) box
  where
    box_nb = box_idx + 1
    accu (cur_slot, cur_value) (_, foc) =
      (cur_slot+1, cur_value + box_nb * cur_slot * foc)



--
--
-- applySequence boxes (Minus w) = boxes'
  -- where
    -- boxes' = boxes//(hash w)







