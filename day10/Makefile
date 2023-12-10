pmine: pipe-maze.py
	python3 pipe-maze.py < input-mine.txt

psmall: pipe-maze.py
	python3 pipe-maze.py < input-small.txt

pmined: pipe-maze.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: pipe-maze.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: pipe-maze.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: pipe-maze.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: pipe-maze
	./pipe-maze < input-mine.txt

optsmall: pipe-maze
	./pipe-maze < input-small.txt

pipe-maze: pipe-maze.hs
	ghc -O2  -o pipe-maze

clean:
	haskell-clean-aux

clear: clean
	rm pipe-maze

.PHONY: mine small opt optsmall clean clear
