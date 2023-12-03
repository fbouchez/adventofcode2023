import sys

max_col = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def check(c):
    # print (f"checking '{c}'")
    num, color = c.strip().split(' ')
    # print (f"couleur detectée: {num} cubes {color}")
    return (int(num) <= max_col[color], (int(num), color))


def check_set(s, maxset):
    cubes = s.split(',')

    setflag = True

    for c in cubes:
        flag, (num, color) = check(c)

        maxset[color] = max (
            maxset[color],
            num
        )

        setflag = setflag and flag


    return setflag


def check_game(l):
    game, reste = l.split(':')

    _,game_idstr = game.split(' ')
    ident = int(game_idstr)

    # print (f"game {ident}: {reste}")

    maxset = {
        "red": 0,
        "green": 0,
        "blue": 0
    }


    sets = reste.split(';')



    gameflag = True

    for s in sets:
        if not check_set(s, maxset):
            gameflag = False

    print ("Game valide:", ident)
    print("Mes max colors:", maxset)

    power = \
        maxset["red"] * \
        maxset["green"] * \
        maxset["blue"]

    print("Mon power:", power)

    if not gameflag:
        retval = 0
    else:
        retval = ident


    return retval, power



def main():
    somme = 0
    spower = 0
    for line in sys.stdin:
        val, power = check_game(line)
        somme += val

        spower += power

    print ("Somme totale:", somme)
    print ("Power total:", spower)








main()
