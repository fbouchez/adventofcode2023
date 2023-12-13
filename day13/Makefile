pmine: incidence-point.py
	python3 incidence-point.py < input-mine.txt

psmall: incidence-point.py
	python3 incidence-point.py < input-small.txt

pmined: incidence-point.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: incidence-point.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: incidence-point.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: incidence-point.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: incidence-point
	./incidence-point < input-mine.txt

optsmall: incidence-point
	./incidence-point < input-small.txt

incidence-point: incidence-point.hs
	ghc -O2 $< -o $@

clean:
	haskell-clean-aux

clear: clean
	rm incidence-point

.PHONY: mine small opt optsmall clean clear
