#!/usr/bin/env python3
import sys
import functools
from enum import Enum
from AoC import *

res1 = 0
res2 = 0

# bad part 1:    248291237
# correct answer 248422077

part2 = True

ordering_p1 = "23456789TJQKA"
ordering_p2 = "J23456789TQKA"

def idx(c):
    if not part2:
        return ordering_p1.index(c)
    else:
        return ordering_p2.index(c)


## Tentative d'utilisation d'enum : quelle horreur !
slist = ['High', 'Pair', 'DoublePair', 'Brelan', 'Full', 'Carre', 'Five']
Strength = Enum('Strength', slist)

Strength.__lt__ = lambda self, x: slist.index(str(self).split('.')[1]) < slist.index(str(x).split('.')[1])

debug ("Carre < Five :", Strength.Carre < Strength.Five )

# Just to be safe, we implement only __eq__ and __lt__ and all other
# comparison functions will be defined
@functools.total_ordering
class Hand:
    def __init__(self,st):
        self.h = st

    def __eq__(self,h2):
        s = self.h
        s2 = h2.h
        return s == s2

    def __lt__(self,h2):
        s = self.h
        s2 = h2.h

        # debug("comparing", s, s2)

        for i in range(5):
            x = s[i]
            y = s2[i]

            # debug(i, x, y)
            # debug("indices:", idx(x), idx(y))

            ix = idx(x)
            iy = idx(y)

            if ix < iy:
                return True
            elif ix > iy:
                return False

        return False


    # def __gt__(self,h2):
        # s = self.h
        # s2 = h2.h
#
        # for i in range(5):
            # x = s[i]
            # y = s2[i]
#
            # debug(i, x, y)
#
            # if idx(x) > idx(y):
                # return True
        # return False


    def __repr__(self):
        return self.h




h=Hand("T75Q2")
k=Hand("936A5")

# print(h < k)
#
# exit(42)



hands = []
for line in sys.stdin:
    line = line.strip()
    hand, sbid = line.split()
    bid = int(sbid)
    hands.append((Hand(hand),bid))


def analyse(hand):
    shand = sorted(hand.h)

    count = 1

    mult = []

    debug("analysing", shand)

    if part2:
        num_jokers = shand.count('J')
        debug("jokers:", num_jokers)
        shand = list(filter(lambda a: a != 'J', shand))
        debug("sand without jokers", shand)


    if shand == []:
        mult = [0]
    else:
        prev = shand[0]

        for c in shand[1:]:
            if c == prev:
                count += 1
            else:
                mult.append(count)
                count = 1
                prev = c

        mult.append(count)

    smult = sorted(mult)

    maxim = smult[-1]
    if part2:
        maxim += num_jokers

    if maxim == 5:
        r = 7
    elif maxim == 4:
        r = 6
    elif maxim == 3:
        second = smult[-2]
        if second == 2:
            r = 5
        else:
            r = 4
    elif maxim == 2:
        second = smult[-2]
        if second == 2:
            r = 3
        else:
            r = 2
    else:
        r = 1

    debug(smult)

    return r

debug (hands)


part2 = False
for part in [1,2]:
    hand_an = []
    for h,b in hands:
        hand_an.append((analyse(h), h, b))

    shands = sorted(hand_an)
    debug(shands)

    res = 0
    for i,htriplet in enumerate(shands):
        val, h, bid = htriplet
        res += (i+1) * bid

    print (f"Valeur partie {part}: {res}")
    part2 = True
