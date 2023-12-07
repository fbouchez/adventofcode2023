pmine: camel-poker.py
	python3 camel-poker.py < input-mine.txt

psmall: camel-poker.py
	python3 camel-poker.py < input-small.txt

pmined: camel-poker.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: camel-poker.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: camel-poker.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: camel-poker.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: camel-poker
	./camel-poker < input-mine.txt

optsmall: camel-poker
	./camel-poker < input-small.txt

camel-poker: camel-poker.hs
	ghc -O2  -o camel-poker

clean:
	haskell-clean-aux

clear: clean
	rm camel-poker

.PHONY: mine small opt optsmall clean clear
