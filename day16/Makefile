pmine: lava-floor.py
	python3 lava-floor.py < input-mine.txt

psmall: lava-floor.py
	python3 lava-floor.py < input-small.txt

pmined: lava-floor.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: lava-floor.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: lava-floor.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: lava-floor.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: lava-floor
	./lava-floor < input-mine.txt

optsmall: lava-floor
	./lava-floor < input-small.txt

lava-floor: lava-floor.hs
	ghc -O2 $< -o $@

clean:
	haskell-clean-aux

clear: clean
	rm lava-floor

.PHONY: mine small opt optsmall clean clear
