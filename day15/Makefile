pmine: lens-library.py
	python3 lens-library.py < input-mine.txt

psmall: lens-library.py
	python3 lens-library.py < input-small.txt

pmined: lens-library.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: lens-library.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: lens-library.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: lens-library.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: lens-library
	./lens-library < input-mine.txt

optsmall: lens-library
	./lens-library < input-small.txt

lens-library: lens-library.hs
	ghc -O2 $< -o $@

clean:
	haskell-clean-aux

clear: clean
	rm lens-library

.PHONY: mine small opt optsmall clean clear
