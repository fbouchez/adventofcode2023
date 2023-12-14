#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0


chmap = []

for line in sys.stdin:
    line = line.strip()
    chmap.append(list(line))


NROWS = len(chmap)
NCOLS = len(chmap[0])


def tilt_north_south_rocks(chmap, d = 'N'):
# def move_north_south_rocks(chmap, r, d='N'):

    if d == 'N':
        dir_r = -1
        st = 0
        end = NROWS
    else:
        st = NROWS-1
        end = -1
        dir_r = 1

    # for c in range(NCOLS):
    for r in range(st, end, -dir_r):
        for c in range(NCOLS):
            ch = chmap[r][c]
            if ch == 'O':
                move_1rock(chmap, r, c, -1, 0)


def move_1rock(chmap, r, c, dir_r, dir_c):
    global res1
    while r>0 and c>0 and r<NROWS-1 and c<NCOLS-1:
        chup = chmap[r+dir_r][c+dir_c]
        if chup == '#' or chup == 'O':
            # on arrête et on en profite pour calculer
            # le résultat de la partie 1 après la boucle
            break
        assert chup == '.'
        chmap[r][c] = '.'
        chmap[r+dir_r][c+dir_c] = 'O'

        r += dir_r
        c += dir_c

    # res1 += (NROWS - r)


def tilt_north(chmap):
    for r in range(NROWS):
        move_north_rocks(chmap, r)


def move_north_rocks(chmap, r):
    for c in range(NCOLS):
        ch = chmap[r][c]
        if ch == 'O':
            move_north_1rock(chmap, r, c)

def move_north_1rock(chmap, r, c):
    global res1
    while r>0:
        chup = chmap[r-1][c]
        if chup == '#' or chup == 'O':
            # on arrête et on en profite pour calculer
            # le résultat de la partie 1 après la boucle
            break
        assert chup == '.'
        chmap[r][c] = '.'
        chmap[r-1][c] = 'O'
        r -= 1

    res1 += (NROWS - r)



def map_in_marbre(chmap):
    return tuple(map(tuple, chmap))



debugcharmap(chmap)
tilt_north(chmap)

print('='*39)
debugcharmap(chmap)

print(map_in_marbre(chmap))


print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
