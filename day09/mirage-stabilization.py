#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0

def analyse_ligne(line):
    nums = [int(x) for x in line.split()]

    n = len(nums)

    mat = [nums]

    while True:

        # generer la ligne suivante
        mat.append([])

        current = mat[-2]
        suivante = mat[-1]

        generate_next(current, suivante)

        debug(suivante)


        # if all(map((0).__eq__, suivante):
        if not any(suivante):
            break

    new_beg = go_up_the_matrix(mat)

    debug(new_beg, mat)

    return mat[0][-1], new_beg


def generate_next(cur, suiv):
    for i in range(len(cur)-1):
        suiv.append(cur[i+1]-cur[i])



def go_up_the_matrix(mat):
    mat[-1].append(0)

    addbeg = 0


    for r in range(len(mat)-1,0,-1):
        add = mat[r][-1]

        mat[r-1].append(
            add +
            mat[r-1][-1]
        )

        new_beg = mat[r-1][0] - addbeg
        debug("premier ligne", r-1, mat[r-1][0])
        debug(f"addbeg for row {r-1} : {new_beg}")
        addbeg = new_beg

    return addbeg













for line in sys.stdin:
    line = line.strip()

    add1, add2 = analyse_ligne(line)

    res1 += add1
    res2 += add2


print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
