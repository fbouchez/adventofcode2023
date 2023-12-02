mine: document-calibration.hs
	runhaskell document-calibration.hs < input-mine.txt

small: document-calibration.hs
	runhaskell document-calibration.hs < input-small.txt


opt: document-calibration
	./document-calibration < input-mine.txt

optsmall: document-calibration
	./document-calibration < input-small.txt

document-calibration: document-calibration.hs
	ghc -O2 document-calibration.hs -o document-calibration


CC=clang
CFLAGS=-g -Wall -Werror

document-calib: document-calib.c

clean:
	haskell-clean-aux

clear: clean
	rm document-calibration

.PHONY: mine small opt optsmall clean clear
