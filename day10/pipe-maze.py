#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0

conv = {
    '.': (),
    '-': ('W','E'),
    '|': ('N','S'),
    '7': ('W','S'),
    'J': ('N','W'),
    'F': ('E','S'),
    'L': ('N','E'),
    'S': ('N','S','E','W')
}

opposite = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

delta_coord = {
    'N': (-1, 0),
    'S': ( 1, 0),
    'E': (0,  1),
    'W': (0, -1),
}


directions = opposite.keys()


mymap = []
charmap = []


row = 0
NCOLS = None

for line in sys.stdin:
    line = line.strip()

    if not NCOLS:
        NCOLS = len(line)
    else:
        assert NCOLS == len(line)


    if 'S' in line:
        col = line.index('S')
        startrow, startcol = row, col

    mymap.append(list(map(lambda c:conv[c],line)))
    charmap.append(list(line))

    row += 1

NROWS = row


def debugcharmap(cm):
    for row in cm:
        debug(''.join(row))

debugcharmap(charmap)


for row in mymap:
    debug(row)

debug("Starting position for animal", startrow, startcol)

def valid(r, c):
    return r >= 0 and c >= 0 and \
        r<NROWS and c<NCOLS


def next_in_dir(row, col, d):
    dr, dc = delta_coord[d]
    nrow = row + dr
    ncol = col + dc
    return nrow, ncol


def neighbours(row, col):
    myneigh = []
    for d in directions:
        nrow, ncol = next_in_dir(row, col, d)


        if not(valid(nrow, ncol)):
            continue


        neighb = mymap[nrow][ncol]

        oppd = opposite[d]

        if oppd in neighb:
            print("Voisin:", d, nrow, ncol, neighb)
            myneigh.append(d)

        else:
            print("NOT Voisin:", d, nrow, ncol, neighb)

    return myneigh



def parcours(row, col, d):

    shadowcharmap = [
        ['.'] * NCOLS for _ in range(NROWS)
    ]

    debugcharmap(shadowcharmap)

    steps = 1

    while True:
        shadowcharmap[row][col] = charmap[row][col]

        nrow, ncol = next_in_dir(row, col, d)
        assert valid(nrow, ncol)
        neighb = mymap[nrow][ncol]

        if nrow == startrow and ncol == startcol:
            break

        oppd = opposite[d]

        assert oppd in neighb

        d1, d2 = neighb

        next_dir = d1 if oppd == d2 else d2

        debug("suivant:", d, nrow, ncol, neighb)


        steps += 1
        row = nrow
        col = ncol
        d = next_dir

    debugcharmap(shadowcharmap)
    return steps, shadowcharmap


start_neigh = neighbours(startrow, startcol)




start_char = None
start_sorted = sorted(start_neigh)
for char in conv:
    if sorted(conv[char]) == start_sorted:
        print("found starting char", char)
        start_char = char
        break


assert start_char


charmap[startrow][startcol] = start_char





total, shadowcharmap = parcours(startrow, startcol, start_neigh[0])

debug("longueur totale:", total)


res1 = total // 2



def find_area(chmap):

    area = 0
    is_in = False
    in_pipe = False

    for row in range(NROWS):
        col = 0

        while col < NCOLS:
            char = chmap[row][col]

            if char == '.':
                assert not in_pipe
                if is_in:
                    chmap[row][col] = 'I'
                    area += 1
                col += 1
                continue

            if char == '|':
                assert not in_pipe
                is_in = not is_in
                col += 1
                continue

            if not in_pipe:
                assert char in "FL"

                in_pipe = True
                if char == 'L':
                    pipe_start = 'N'
                else:
                    pipe_start = 'S'

            else:
                assert char in '-J7' # on continue le tuyau

                if char == '-': # on continue le tuyau
                    pass

                else:
                    in_pipe = False
                    if char == 'J':
                        pipe_end = 'N'
                    else:
                        pipe_end = 'S'

                    # fin du pipe
                    # vérification si séparation

                    if pipe_start != pipe_end:
                        is_in = not is_in

            col += 1

    return area






res2 = find_area(shadowcharmap)

debugcharmap(shadowcharmap)





print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
