#!/usr/bin/env python3
import sys
from AoC import *

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
    for i in range(1,len(chunk)):
        # tester entre la row i et la i-1
        if is_reflection(chunk, i):
            return i

    return None

def is_reflection(chunk, i):
    row_after = len(chunk)-i
    row_before = i
    for delta_i in range(0, min(row_after, row_before)):
        if chunk[i+delta_i] != chunk[i-1-delta_i]:
            return False
    return True


def find_vert_reflection(chunk):
    ch2 = transpose(chunk)
    return find_horiz_reflection(ch2)


def find_reflection(chunk):
    res = find_horiz_reflection(chunk)
    if res != None:
        return 100 * res

    res = find_vert_reflection(chunk)

    if res == None:
        print("Could not find reflection in following chunk:")
        showchunk(chunk)
        exit(1)
    return res



for ch in chunks:
    # res1 += find_horiz_reflection(ch)
    res1 += find_reflection(ch)

print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
