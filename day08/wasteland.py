#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0

part2 = True

instructions = input().strip()
l=input().strip()
assert l == ""

network = {}

for line in sys.stdin:
    line = line.strip()
    node, voisins = line.split(' = ')

    vgauche, vdroit = voisins[1:-1].split(', ')

    network[node] = (vgauche, vdroit)


debug(network)



def find_next(node, cur_inst):
    if cur_inst == 'L':
        return network[node][0]
    elif cur_inst == 'R':
        return network[node][1]
    else:
        raise ValueError

def fini(node_list):
    return all(map(lambda x: x.endswith('Z'), node_list))



def find_cycle(start_node):

    steps = 0
    i_instr = 0
    visited = {}

    current = start_node

    # visited.add((current, i_instr))

    visited[(current, i_instr)] = steps

    endings = []
    found_ending = False

    while True:
        steps += 1

        cur_inst = instructions[i_instr]
        nextnode = find_next(current, cur_inst)

        i_instr += 1
        i_instr %= len(instructions)

        if (nextnode, i_instr) in visited:
            debug("cycle found !!!!")


            # assert # ne pas oublier de soustraire pour 'Z'

            previous_steps = visited[(nextnode, i_instr)]

            demarrage = previous_steps-1
            debug("Démarrage avant cycle:", demarrage)
            longueur = steps - previous_steps
            debug("longueur du cycle:", longueur)
            debug("endings:", endings)

            # assert len(endings) == 1
            # assert endings[0] == longueur

            return demarrage, longueur

        if nextnode[-1] == 'Z':
            found_ending = True
            endings.append(steps)
            print("Found one ending at steps", steps)


        visited[(nextnode, i_instr)] = steps
        if found_ending:
            debug("Visiting after ending", nextnode, i_instr, steps)

        current = nextnode



if not part2:
    start = ['AAA']
else:
    start = list(filter(lambda x: x.endswith('A'), network.keys()))
    debug ("starting positions:", start)

current = list(start)


cycles = list(map(find_cycle, start))

print(cycles)


def prim(n,m):
    # compteur qui compte le nombre de diviseurs communs à m et n
    nombreDiv = 0
    for i in range(1,n+1):
        # Si i est un diviseur commun à m et n on incrémente le compteur nombrDiv
        if ( m%i == 0 and n%i == 0):
            nombreDiv = nombreDiv + 1
        # Si le nombre des diviseurs communs à m et n est = 1
        # alors m et n sont premiers entre eux
    if (nombreDiv  == 1):
        return True
    else:
        return False

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


factors = []
for (d,l) in cycles:
    pf = prime_factors(l)
    print("facteurs:", pf)
    factors.append(pf)

    # for (d2, l2) in cycles:
        # if l != l2:
            # print("premiers?", l, l2, prim(l,l2))


def check_cycle(c, steps):
    start, longueur = c
    return (steps - start) % longueur == 0



res2 = factors[0][1]

for f in factors:
    debug("mult by", f[0])
    res2 *= f[0]



print ("Valeur partie 2:", res2)







onestart, onelongueur = cycles.pop()
onefactors = factors.pop()

commonfactor = onefactors[1]
onefactor = onefactors[0]

num_cycles = 1






exit(42)

while True:
    steps = onestart + num_cycles*onelongueur

    debug("testing:", steps)

    if all(map(lambda c: check_cycle(c, steps), cycles)):
        print("trouvé:", steps)
        exit(0)

    num_cycles += 1




    # steps += 1
    # cur_inst = instructions[i_instr]
#
    # current = map (lambda x: find_next(x, cur_inst), current)
#
    # current = list(current)
    # debug(current)
#
#
    # i_instr += 1
    # i_instr %= len(instructions)




print ("Valeur partie 1:", steps)
print ("Valeur partie 2:", res2)

