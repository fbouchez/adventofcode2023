pmine: hot-springs.py
	python3 hot-springs.py < input-mine.txt

psmall: hot-springs.py
	python3 hot-springs.py < input-small.txt

pmined: hot-springs.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: hot-springs.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: hot-springs.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: hot-springs.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: hot-springs
	./hot-springs < input-mine.txt

optsmall: hot-springs
	./hot-springs < input-small.txt

hot-springs: hot-springs.hs
	ghc -O2 $<  -o hot-springs

clean:
	haskell-clean-aux

clear: clean
	rm hot-springs

.PHONY: mine small opt optsmall clean clear
