mine: seeds.hs
	runhaskell seeds.hs < input-mine.txt

small: seeds.hs
	runhaskell seeds.hs < input-small.txt

pymine: seeds.py
	python3 seeds.py < input-mine.txt

pysmall: seeds.py
	python3 seeds.py < input-small.txt



opt: seeds
	./seeds < input-mine.txt

optsmall: seeds
	./seeds < input-small.txt

seeds: seeds.hs
	ghc -O2  -o seeds

clean:
	haskell-clean-aux

clear: clean
	rm seeds

.PHONY: mine small opt optsmall clean clear
