import sys

res1 = 0
res2 = 0

seeds = []

current_map = None

maps = {}


order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]



for line in sys.stdin:
    line = line.strip()
    if not line:
        current_map = None
        continue

    if line.startswith("seeds: "):
        _,s = line.split(": ")
        seeds = [int(x) for x in s.split()]
        continue

    if line.endswith("map:"):
        m,_ = line.split()
        source,_,dest = m.split('-')


        maps[(source,dest)] = []
        current_map = maps[(source,dest)]
        continue


    assert current_map != None


    print ("line:", line)
    idx_dest, idx_source, rng = [int(x) for x in line.split()]

    # triplet : debut source , fin source, décalage
    # à appliquer
    current_map.append((idx_source, idx_source+rng-1, idx_dest - idx_source))

print (maps)




def seedToLoc(x):
    for i in range(len(order)-1):
        x = applyorder(order[i], order[i+1], x)
    return x


def applyorder(src, dst, seed):
    mymap = maps[(src,dst)]

    flag = False

    out_seed=seed
    print('='*80)
    print(f"Seed en cours de {src} vers {dst}:",seed)
    for (idx_deb, idx_fin, offset) in mymap:
        if (idx_deb <= seed) and (seed <= idx_fin):
            print("range trouvé:", idx_deb, idx_fin, offset)
            assert not flag
            out_seed = seed+offset
            flag = True

    return out_seed







print(f"{seeds=}")
location = list(map(seedToLoc, seeds))
print(f"{location=}")


res1 = min(location)
print ("Valeur partie 1:", res1)
print ("Valeur partie 2:", res2)
