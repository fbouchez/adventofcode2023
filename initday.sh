#!/bin/bash

if [[ "x$1" == "x-h" ]] ; then
  echo "Usage $0"
  echo -e "\tPrepare current directory for today's AoC puzzle"
  echo -e "\tSelect example input first (triple click in example box)"
  echo -e "\tthen run this script and follow instructions."
  exit 0
fi


f="input-small.txt"
echo "Will use the following as small input (triple click in example box):"
xclip -o
echo -e "--EOF"
read -p "Press <enter> to validate or C-c to abort."
xclip -o > $f

f="input-mine.txt"
echo -e "--EOF\nNow put regular input in clipboard and press <enter>"
read
xclip -o
xclip -o > $f
echo -e "--EOF\nContents saved in $f"


f="AoC.hs"
if [[ -L $f ]]; then
  echo "Link already exists: $f"
else
  echo "Linking $f"
  ln -s ../Haskell/AoC.hs
fi

echo -n "Enter filename for today's puzzle: "
read execname
filename=$execname.hs
if [[ -e $filename ]]; then
  echo "$filname already exists"
else
  echo "Copying template to ${filename}"
  cp ../Haskell/template.hs ${filename}
fi

if [[ -e "Makefile" ]]; then
  echo "Makefile already exists"
else
  echo "Creating Makefile"
  cat <<EOF > Makefile
mine: ${filename}
	runhaskell ${filename} < input-mine.txt

small: ${filename}
	runhaskell ${filename} < input-small.txt


opt: ${execname}
	./${execname} < input-mine.txt

optsmall: ${execname}
	./${execname} < input-small.txt

${execname}: ${filename}
	ghc -O2 ${filename} -o ${execname}

clean:
	haskell-clean-aux

clear: clean
	rm $execname

.PHONY: mine small opt optsmall clean clear
EOF
fi

function yes_or_no {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) echo "Aborted" ; return  1 ;;
        esac
    done
}


yes_or_no "Do you want to commit files in git?"
ret=$?

if [[ $ret -eq 1 ]]; then
  exit 0;
fi

echo "Initial adding of files in git."
git add AoC.hs ${filename} Makefile input-small.txt 
git ci -m 'Initial commit for $execname'
