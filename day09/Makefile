pmine: mirage-stabilization.py
	python3 mirage-stabilization.py < input-mine.txt

psmall: mirage-stabilization.py
	python3 mirage-stabilization.py < input-small.txt

pmined: mirage-stabilization.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: mirage-stabilization.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: mirage-stabilization.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: mirage-stabilization.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: mirage-stabilization
	./mirage-stabilization < input-mine.txt

optsmall: mirage-stabilization
	./mirage-stabilization < input-small.txt

mirage-stabilization: mirage-stabilization.hs
	ghc -O2  -o mirage-stabilization

clean:
	haskell-clean-aux

clear: clean
	rm mirage-stabilization

.PHONY: mine small opt optsmall clean clear
