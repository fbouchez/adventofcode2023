import sys

res1 = 0
res2 = 0


copies = 1

scratch = []

for line in sys.stdin:
    line = line.strip()
    _, rst = line.split(": ")
    win, all_ = rst.split(" | ")

    wins = [int(x) for x in win.split()]
    alls = [int(x) for x in all_.split()]

    vrai = []
    for w in wins:
        if w in alls:
            vrai.append(w)

    scratch.append(len(vrai))

    if len(vrai) == 0:
        points = 0
    else:
        points = 2**(len(vrai)-1)

    print (wins, alls, points)
    res1 += points


print ("Valeur partie 1:", res1)


print ("scratch", scratch)


nb_copies = [1] * len(scratch)

for i,s in enumerate(scratch):
    num_current = nb_copies[i]

    for card in range(i+1, i+s+1):
        print ("card num:", card)
        nb_copies[card] += num_current


print ("copies:", nb_copies)
res2 = sum(nb_copies)

print ("Valeur partie 2:", res2)
