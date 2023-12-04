mine: scratchcards.hs
	runhaskell scratchcards.hs < input-mine.txt

small: scratchcards.hs
	runhaskell scratchcards.hs < input-small.txt

pymine: scratchcards.py
	python3 scratchcards.py < input-mine.txt

pysmall: scratchcards.py
	python3 scratchcards.py < input-small.txt



opt: scratchcards
	./scratchcards < input-mine.txt

optsmall: scratchcards
	./scratchcards < input-small.txt

scratchcards: scratchcards.hs
	ghc -O2  -o scratchcards

clean:
	haskell-clean-aux

clear: clean
	rm scratchcards

.PHONY: mine small opt optsmall clean clear
