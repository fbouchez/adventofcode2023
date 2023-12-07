#!/usr/bin/env python3
import sys
from math import sqrt, ceil, floor
from AoC import debug

res1 = 0
res2 = 0

time = None
dist = None

def parseline(l):
    nums = l.split()[1:]

    part1 = map(int, nums)
    part2 = [int(''.join(nums))]

    return part1, part2



time1, time2 = parseline(input())
dist1, dist2 = parseline(input())

part1 = zip(time1, dist1)
part2 = zip(time2, dist2)

# debug(list(part1))
# debug(list(part2))

def best_races(r):
    t, d = r
    possib = [(h, t) for h in range(1,t)]
    debug("possibles", possib)
    distances = list(map(computeDist,possib))
    win = list(filter( lambda x: x>d, distances))

    return win


def computeDist(c):
    (holdtime, totaltime) = c
    return holdtime * (totaltime - holdtime)




def equation(t, d):

    delta = t*t - 4*d

    sdelta = sqrt(delta)

    sol1 = (t - sdelta) / 2
    sol2 = (t + sdelta) / 2

    debug(sol1, sol2)
    debug (sol2 - sol1)

    csol1 = ceil(sol1)
    fsol2 = floor(sol2)

    start = int(sol1)+1 if csol1 == sol1 else csol1
    end   = int(sol2)-1 if fsol2 == sol2 else fsol2

    return end - start + 1


# -x² + tx - d = 0
#
# delta = t²
#
# ax² + bx + c
#
# -b ± sqrt(delta) / 2
# delta = b² - 4ac


res1 = 1
for r in part1:
    debug("computing race", r)
    races = best_races(r)

    eqrace = equation(*r)

    debug(f"Brute: {len(races)} vs equation {eqrace}")
    assert len(races) == eqrace
    res1 *= eqrace

print ("Valeur partie 1:", res1)


res2 = equation(*next(part2))
print ("Valeur partie 2:", res2)
