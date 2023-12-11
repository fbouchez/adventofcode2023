#!/usr/bin/env python3
import sys
from AoC import *
# from math import abs

res1 = 0
res2 = 0

space = []

NROWS = 0
NCOLS = None
for line in sys.stdin:
    NROWS += 1
    line = line.strip()

    if not NCOLS:
        NCOLS = len(line)
    else:
        assert NCOLS == len(line)

    space.append(list(line))
    if '#' not in line:
        debug("duplique")
        NROWS += 1
        space.append(list(line))


def  debugespace(esp):
    for r in esp:
        debug(''.join(r))



debug("taille de l'espace avant expansion:", NROWS, NCOLS)

col = 0
while col < NCOLS:

    cdup = True
    for r in range(NROWS):
        if space[r][col] == '#':
            cdup = False
            break

    if not cdup:
        col += 1
        continue

    NCOLS += 1
    for r in range(NROWS):
        space[r].insert(col, '.')

    col += 2



debugespace(space)

debug("taille de l'espace avant expansion:", NROWS, NCOLS)


galaxies = []

for r in range(NROWS):
    for c in range(NCOLS):
        if space[r][c] == '#':
            galaxies.append((r,c))


debug("galaxies:",  galaxies)



def shortestPath(ga, gb):
    ra, ca = ga
    rb, cb = gb

    return abs(ra-rb) + abs(ca-cb)



shortest_paths = []

while len(galaxies) > 1:
    ga = galaxies.pop()

    for gb in galaxies:
        shortest_paths.append(shortestPath(ga, gb))




res1 = sum(shortest_paths)




print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
