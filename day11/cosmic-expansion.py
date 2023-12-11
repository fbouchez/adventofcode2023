#!/usr/bin/env python3
import sys
from AoC import *
# from math import abs

res1 = 0
res2 = 0

space = []

# TAILLE_INTERSIDERALE = 2
# TAILLE_INTERSIDERALE = 10
TAILLE_INTERSIDERALE = 1_000_000


NROWS = 0
NCOLS = None
for line in sys.stdin:
    NROWS += 1
    line = line.strip()

    if not NCOLS:
        NCOLS = len(line)
    else:
        assert NCOLS == len(line)

    if '#' not in line:
        # debug("duplique")
        debug("vide intersidéral")
        # NROWS += 1
        space.append(['-'] * len(line))
    else:
        space.append(list(line))

def  debugespace(esp):
    for r in esp:
        debug(''.join(r))



# debug("taille de l'espace avant expansion:", NROWS, NCOLS)

col = 0
for c in range(NCOLS):
    vide = True
    for r in range(NROWS):
        if space[r][c] == '#':
            vide = False
            break

    if not vide:
        continue

    for r in range(NROWS):
        space[r][c] = '|'




debugespace(space)

debug("taille de l'espace avant expansion:", NROWS, NCOLS)


galaxies = []

for r in range(NROWS):
    for c in range(NCOLS):
        if space[r][c] == '#':
            galaxies.append((r,c))


debug("galaxies:",  galaxies)



def shortestPath(ga, gb):
    debug(f"computing shortest_paths betwen {ga} and {gb}")
    ra, ca = ga
    rb, cb = gb

    dist_r = abs(ra-rb)

    dist_c = abs(ca-cb)

    dir_r = 0 if not dist_r else (rb-ra) // dist_r
    dir_c = 0 if not dist_c else (cb-ca) // dist_c


    r, c = ra, ca

    real_dist_r = 0
    real_dist_c = 0


    x = r
    xtarget = rb
    dir_x = dir_r

    horiz = False

    real_dist = 0

    for _ in range(2):
        while x != xtarget:
            x += dir_x

            if not horiz:
                debug("space vert at", x, c)
                sp = space[x][c]
            else:
                debug("space horiz at", r, x)
                sp = space[r][x]

            if sp == '.' or sp == '#':
                real_dist += 1
            elif sp == '|' or sp == '-':
                real_dist += TAILLE_INTERSIDERALE
            else:
                raise ValueError

        if horiz:
            break

        r = rb
        x = c
        xtarget = cb
        dir_x = dir_c
        horiz = True

        real_dist_r = real_dist
        real_dist = 0

    real_dist_c = real_dist

    return real_dist_r + real_dist_c
#
    # debug(f"de {ga} à {gb} direction {dir_r} et {dir_c}")




shortest_paths = []

while len(galaxies) > 1:
    ga = galaxies.pop()

    for gb in galaxies:
        shortest_paths.append(shortestPath(ga, gb))




res1 = sum(shortest_paths)




print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
