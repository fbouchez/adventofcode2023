pmine: wasteland.py
	python3 wasteland.py < input-mine.txt

psmall: wasteland.py
	python3 wasteland.py < input-small.txt

pmined: wasteland.py
	loopwait 'python3 $< -d < input-mine.txt' $<

psmalld: wasteland.py
	loopwait 'python3 $< -d < input-small.txt' $<

mined: wasteland.hs
	loopwait 'runhaskell $< < input-mine.txt' $<

smalld: wasteland.hs
	loopwait 'runhaskell $< < input-small.txt' $<

optmine: wasteland
	./wasteland < input-mine.txt

optsmall: wasteland
	./wasteland < input-small.txt

wasteland: wasteland.hs
	ghc -O2  -o wasteland

clean:
	haskell-clean-aux

clear: clean
	rm wasteland

.PHONY: mine small opt optsmall clean clear
