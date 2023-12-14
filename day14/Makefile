pmine: reflector-dish.py
	python3 reflector-dish.py < input-mine.txt

psmall: reflector-dish.py
	python3 reflector-dish.py < input-small.txt

pmined: reflector-dish.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: reflector-dish.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: reflector-dish.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: reflector-dish.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: reflector-dish
	./reflector-dish < input-mine.txt

optsmall: reflector-dish
	./reflector-dish < input-small.txt

reflector-dish: reflector-dish.hs
	ghc -O2 $< -o $@

clean:
	haskell-clean-aux

clear: clean
	rm reflector-dish

.PHONY: mine small opt optsmall clean clear
