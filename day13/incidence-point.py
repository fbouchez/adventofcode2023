#!/usr/bin/env python3
import sys
from AoC import *

from operator import ne

res1 = 0
res2 = 0

all_in = sys.stdin.read()

chunks_raw = all_in.split('\n\n')

chunks = list(map(lambda c: c.split('\n'), chunks_raw))


def showchunk(chunk):
    for r in chunk:
        print(r)

for c in chunks:
    showchunk(c)
    print('='*39)


def transpose(chunk):
    return list(zip(*chunk))


def find_horiz_reflection(chunk):
    i_part1 = None
    i_part2 = None
    for i in range(1,len(chunk)):
        # tester entre la row i et la i-1
        part1, part2 =  is_reflection(chunk, i)
        if part1:
            i_part1 = i
        if part2:
            i_part2 = i

    return i_part1, i_part2


def differences(l1, l2):
    return sum(map(ne, l1, l2))


def is_reflection(chunk, i):
    row_after = len(chunk)-i
    row_before = i

    num_smudges = 0

    for delta_i in range(0, min(row_after, row_before)):
        diff = differences(chunk[i+delta_i], chunk[i-1-delta_i])
        num_smudges += diff
        if num_smudges > 1:
            return (False, False)

    if num_smudges == 0:
        return (True, False)
    assert num_smudges == 1

    return (False, True)


def find_vert_reflection(chunk):
    ch2 = transpose(chunk)
    return find_horiz_reflection(ch2)


def find_reflection(chunk):
    ipart1, ipart2 = find_horiz_reflection(chunk)

    res1 = 0
    res2 = 0

    if ipart1 != None:
        res1 = 100*ipart1
    if ipart2 != None:
        res2 = 100*ipart2

    ipart1, ipart2 = find_vert_reflection(chunk)

    if ipart1 != None:
        assert res1 == 0
        res1 = ipart1
    if ipart2 != None:
        assert res2 == 0
        res2 = ipart2

    if res1 == 0 and res2 == 0:
        print("Could not find reflection in following chunk:")
        showchunk(chunk)
        exit(1)
    return res1, res2



for ch in chunks:
    # res1 += find_horiz_reflection(ch)
    r1,r2 = find_reflection(ch)
    res1 += r1
    res2 += r2

print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
