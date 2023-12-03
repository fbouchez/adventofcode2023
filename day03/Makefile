mine: engine.hs
	runhaskell engine.hs < input-mine.txt

small: 
	runhaskell  < input-small.txt

pymine: engine.py
	python3 engine.py < input-mine.txt

pysmall: engine.py
	python3 engine.py < input-small.txt



opt: engine
	./engine < input-mine.txt

optsmall: engine
	./engine < input-small.txt

engine: engine.hs
	ghc -O2  -o engine

clean:
	haskell-clean-aux

clear: clean
	rm engine

.PHONY: mine small opt optsmall clean clear
