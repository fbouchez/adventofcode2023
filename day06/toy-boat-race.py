import sys

res1 = 0
res2 = 0

time = None
dist = None

for line in sys.stdin:
    line = line.strip()
    l = [int(x) for x in line.split()[1:]]
    # l.pop(0)

    if time == None:
        time = l
    else:
        dist = l


def best_races(t, d):

    possib = [(h, t) for h in range(1,t)]

    print(possib)

    distances = list(map(computeDist,possib))

    win = list(filter( lambda x: x>d, distances))

    return win


def computeDist(c):
    (holdtime, totaltime) = c
    return holdtime * (totaltime - holdtime)



print (time)
print (dist)


res1 = 1
for r in range(len(time)):
    races = best_races(time[r], dist[r])

    print(races)
    
    res1 *= len(races)

print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
