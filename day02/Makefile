mine: cube-conundrum.hs
	runhaskell cube-conundrum.hs < input-mine.txt

small: cube-conundrum.hs
	runhaskell cube-conundrum.hs < input-small.txt


opt: cube-conundrum
	./cube-conundrum < input-mine.txt

optsmall: cube-conundrum
	./cube-conundrum < input-small.txt

cube-conundrum: cube-conundrum.hs
	ghc -O2 cube-conundrum.hs -o cube-conundrum

clean:
	haskell-clean-aux

clear: clean
	rm cube-conundrum

.PHONY: mine small opt optsmall clean clear
