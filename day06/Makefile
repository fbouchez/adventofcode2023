mine: toy-boat-race.hs
	runhaskell toy-boat-race.hs < input-mine.txt

small: toy-boat-race.hs
	runhaskell toy-boat-race.hs < input-small.txt

pmine: toy-boat-race.py
	python3 toy-boat-race.py < input-mine.txt

psmall: toy-boat-race.py
	python3 toy-boat-race.py < input-small.txt

psmalld: toy-boat-race.py
	loopwait 'python3 toy-boat-race.py -d < input-small.txt' toy-boat-race.py

pmined: toy-boat-race.py
	loopwait 'python3 toy-boat-race.py -d < input-mine.txt' toy-boat-race.py




opt: toy-boat-race
	./toy-boat-race < input-mine.txt

optsmall: toy-boat-race
	./toy-boat-race < input-small.txt

toy-boat-race: toy-boat-race.hs
	ghc -O2  -o toy-boat-race

clean:
	haskell-clean-aux

clear: clean
	rm toy-boat-race

.PHONY: mine small opt optsmall clean clear
