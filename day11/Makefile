pmine: cosmic-expansion.py
	python3 cosmic-expansion.py < input-mine.txt

psmall: cosmic-expansion.py
	python3 cosmic-expansion.py < input-small.txt

pmined: cosmic-expansion.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: cosmic-expansion.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: cosmic-expansion.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: cosmic-expansion.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: cosmic-expansion
	./cosmic-expansion < input-mine.txt

optsmall: cosmic-expansion
	./cosmic-expansion < input-small.txt

cosmic-expansion: cosmic-expansion.hs
	ghc -O2  -o cosmic-expansion

clean:
	haskell-clean-aux

clear: clean
	rm cosmic-expansion

.PHONY: mine small opt optsmall clean clear
