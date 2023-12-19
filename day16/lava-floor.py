#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0

chmap, NROWS, NCOLS = scan_char_map()


def valid(r, c):
    return 0 <= r < NROWS and 0 <= c < NCOLS

debugcharmap(chmap)

print('='*39)

seen = {
    'N': False,
    'S': False,
    'E': False,
    'W': False,
}


shadowmap = None


def initshadowmap():
    global shadowmap
    shadowmap = [
        [dict(seen) for _ in range(NCOLS)] for _ in range(NROWS)
    ]


def seenToCh (seen):
    ch = None
    for d in seen:
        if seen[d]:
            if ch:
                ch = '+'
            else:
                ch = dirch[d]
    if ch:
        return ch
    else:
        return '.'



def debugshadowmap(sm):
    for row in sm:
        debug(''.join(map(seenToCh, row)))


turn_back = {  # '\'
    'N': 'W',
    'W': 'N',
    'E': 'S',
    'S': 'E',
}

turn_slash = { # '/'
    'N': 'E',
    'E': 'N',
    'S': 'W',
    'W': 'S',
}

dirch = {
    'N': '^',
    'E': '>',
    'S': 'v',
    'W': '<',
}


chdir = {
    '^': 'N',
    '>': 'E',
    'v': 'S',
    '<': 'W',
}

splits = {  # '\'
    'N': ('E','W'),
    'S': ('E','W'),
    'E': ('N','S'),
    'W': ('N','S'),
}


already_passed = {
    'N': '^|',
    'E': '>-',
    'S': 'v|',
    'W': '<-',
}


def update_shadow_map(r, c, d):
    global shadowmap

    if not valid(r,c):
        return False

    seen = shadowmap[r][c]

    if seen[d]:
        return False

    seen[d] = True
    return True


def explore(r, c, d):

    global shadowmap

    while True:

        if not update_shadow_map(r, c, d):
            return

        cur = chmap[r][c]

        if cur == '.' or \
           (cur == '-' and (d in "EW")) or \
           (cur == '|' and (d in "NS")) :

            r, c = next_in_dir(r, c, d)
            continue

        if cur in '/\\':
            if cur == '\\':
                d = turn_back[d]
            elif cur == '/':
                d = turn_slash[d]
            r, c = next_in_dir(r, c, d)
            continue

        assert cur in '-|'

        if cur == '-':
            assert d in 'NS'
        if cur == '|':
            assert d in 'EW'
        break


    d1, d2 = splits[d]

    r1, c1 = next_in_dir(r, c, d1)
    explore(r1, c1, d1)
    r2, c2 = next_in_dir(r, c, d2)
    explore(r2, c2, d2)



def explore_get_max(r, c, d, curmax):
    initshadowmap()

    explore(r, c, d)
    cur = compute_sol()
    # print("Solution pour", r, c, d, cur)

    if cur > curmax:
        print("plus grand", cur)
        curmax = cur
    return curmax


def explore_all():
    curmax = 0

    for r in range(NROWS):
        for c,d in [(0,'E'), (NCOLS-1, 'W')]:
            curmax = explore_get_max(r, c, d, curmax)

    for c in range(NCOLS):
        for r,d in [(0,'S'), (NROWS-1, 'N')]:
            curmax = explore_get_max(r, c, d, curmax)

    return curmax

    # debugshadowmap(shadowmap)


def compute_sol():
    res = 0
    for r in range(NROWS):
        for c in range(NCOLS):
            seen = shadowmap[r][c]
            for d in seen:
                if seen[d]:
                    res += 1
                    break
    return res


initshadowmap()
explore(0,0,'E')
res1 = compute_sol()
print ("Valeur partie 1:", res1)

res2 = explore_all()
print ("Valeur partie 2:", res2)
