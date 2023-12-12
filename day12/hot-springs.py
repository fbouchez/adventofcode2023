#!/usr/bin/env python3
import sys
from AoC import *

res1 = 0
res2 = 0

springs = []

for line in sys.stdin:
    line = line.strip()
    field,svalues = line.split()
    values = [int(x) for x in svalues.split(',')]

    springs.append((list(field), values))


debug(springs)


def possibilities(r):
    field, values = r

    ret = poss_rec(field, 0, values, 0)

    debug("Row", ''.join(field), values, " : ", ret)
    return ret


def poss_rec(field, idxf, values, idxv):
    """
    Renvoie le nombre de possibilités à partir des
    indices idxf pour field et idxv pour values
    """

    debug("appel rec sur:", ''.join(field), idxf, values, idxv)

    # si on a tout consommé
    assert idxf <= len(field)
    if idxf == len(field):
        if idxv == len(field):
            return 1
        else:
            return 0



    char = field[idxf]
    while (char == '.'):
        idxf += 1
        if idxf == len(field):
            break
        char = field[idxf]

    if idxf == len(field):
        # on a tout scanné sans trouver de dysfonctionnement
        if idxv == len(values):
            return 1
        else:
            return 0

    # on est sur un '#' ou un '?'

    if char == '#':
        if idxv == len(values):
            return 0

        assert idxv < len(values) # à mon avis non
        # sinon on return 0 si ça arrive : à vérifier

        v = values[idxv]
        idxv += 1

        while (char == '#' or char == '?') and v > 0:
            idxf += 1
            v -= 1
            if idxf == len(field):
                break
            char = field[idxf]

        if idxf == len(field):
            if v == 0:
                if idxv == len(values):
                    return 1
                else:
                    return 0
            else:
                return 0

        # on n'est pas à la fin du field

        if v == 0: # valeur toute consommée
            if char == '#':
                return 0
            elif char == '.' or char == '?': # super, ça va jusqu'à présent
                return poss_rec(field, idxf+1, values, idxv)
            else:
                raise Exception

        assert v > 0 # il en manque
        assert char == '.'
        return 0


    assert char == '?'

    # on teste les deux possibilités
    field[idxf] = '.'
    poss_point = poss_rec(field, idxf, values, idxv)

    field[idxf] = '#'
    poss_diese = 0

    if idxv == len(values):
        poss_diese += 0
    elif values[idxv] == 1:
        if idxf+1 == len(field):
            poss_diese += 1
        else:
            nextch = field[idxf+1]
            if nextch == '.' or nextch == '?':
                debug("mon cas ici")
                poss_diese += poss_rec(field, idxf+2, values, idxv+1)
                debug("valeur après retour:", poss_diese)

            else:
                assert nextch == '#'
                poss_diese += 0
    else:
        poss_diese = poss_rec(field, idxf, values, idxv)

    field[idxf] = '?'

    return poss_point + poss_diese














for r in springs:
    res1 += possibilities(r)



print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
