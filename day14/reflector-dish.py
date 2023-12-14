#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0


chmap = []

for line in sys.stdin:
    line = line.strip()
    chmap.append(list(line))


initial_copy = list(map(list,chmap))


NROWS = len(chmap)
NCOLS = len(chmap[0])

def north_load(chmap):
    x = 0
    for r in range(NROWS):
        for c in range(NCOLS):
            if chmap[r][c] == 'O':
                x += (NROWS - r)
    return x



def tilt_north_south_rocks(chmap, d = 'N'):
# def move_north_south_rocks(chmap, r, d='N'):

    if d == 'N':
        dir_r = -1
        st = 0
        end = NROWS
    else:
        dir_r = 1
        st = NROWS-1
        end = -1

    for r in range(st, end, -dir_r):
        for c in range(NCOLS):
            ch = chmap[r][c]
            if ch == 'O':
                move_1rock(chmap, r, c, dir_r, 0)


def tilt_west_east_rocks(chmap, d = 'W'):

    if d == 'W':
        dir_c = -1
        st = 0
        end = NCOLS
    else:
        dir_c = 1
        st = NCOLS-1
        end = -1

    for c in range(st, end, -dir_c):
        for r in range(NROWS):
            ch = chmap[r][c]
            if ch == 'O':
                move_1rock(chmap, r, c, 0, dir_c)



def move_1rock(chmap, r, c, dir_r, dir_c):
    global res1
    rd = r+dir_r
    cd = c+dir_c

    while rd>=0 and cd>=0 and rd<=NROWS-1 and cd<=NCOLS-1:
        chup = chmap[rd][cd]
        if chup == '#' or chup == 'O':
            # on arrête et on en profite pour calculer
            # le résultat de la partie 1 après la boucle
            break
        assert chup == '.'
        chmap[r][c] = '.'
        chmap[rd][cd] = 'O'

        r = rd
        c = cd
        rd = r+dir_r
        cd = c+dir_c

    # res1 += (NROWS - r)


def tilt_north(chmap):
    tilt_north_south_rocks(chmap, 'N')

def tilt_south(chmap):
    tilt_north_south_rocks(chmap, 'S')

def tilt_west(chmap):
    tilt_west_east_rocks(chmap, 'W')

def tilt_east(chmap):
    tilt_west_east_rocks(chmap, 'E')

def tilt_cycle(chmap):
    tilt_north(chmap)
    tilt_west(chmap)
    tilt_south(chmap)
    tilt_east(chmap)

def map_in_marbre(chmap):
    return tuple(map(tuple, chmap))



debugcharmap(chmap)

cycles = 0

memory = {
    map_in_marbre(chmap): 0
}

longueur_cycle = None
init_cycle = None

while True:
    tilt_cycle(chmap)
    cycles += 1
    mm = map_in_marbre(chmap)

    # debugcharmap(mm)

    if mm in memory:
        print('='*39)
        print("Cycle trouvé au temps", cycles)

        prev_cycle = memory[mm]
        debugcharmap(mm)

        print("Vu pour la dernière fois au temps", prev_cycle)

        longueur_cycle = cycles - prev_cycle
        init_cycle = prev_cycle

        break

    memory[mm] = cycles



target = 1_000_000_000

nb_cycle = (target - init_cycle) // longueur_cycle
reste = target - init_cycle - (nb_cycle * longueur_cycle)

print(f"Target: {target} = init {init_cycle} + {nb_cycle}x{longueur_cycle} + {reste}")

for _ in range(reste):
    tilt_cycle(chmap)

print("Etat final:")
debugcharmap(chmap)







# tilt_cycle(chmap)
# print('='*39)
# debugcharmap(chmap)
#


# print(map_in_marbre(chmap))
#

tilt_north(initial_copy)
res1 = north_load(initial_copy)

res2 = north_load(chmap)

print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
