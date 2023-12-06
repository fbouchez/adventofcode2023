import sys

# part2 = False
part2 = True

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
        s = [int(x) for x in s.split()]

        print("longueur:", len(s))

        if not part2:
            for seed in s:
                seeds.append((seed, seed))
            continue

        else:
            for i in range(len(s)//2):
                st = s[2*i]
                ln = s[2*i+1]
                seeds.append((st, st+ln-1))
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

smaps = {}
for m in maps.keys():
    smaps[m] = sorted(maps[m])


print(smaps)


print("seeds:", seeds)

sseeds = sorted(seeds)

print("sorted seeds:", sseeds)


def seedToLoc(seeds):

    x = seeds
    for i in range(len(order)-1):
        x = applyorder(order[i], order[i+1], x)
        x = sorted(x)
    return x


def applyorder(src, dst, cur_rng_lst):
    print ('='*80)
    print (f"applying {src} to {dst} to list {cur_rng_lst}")

    mymap = smaps[(src,dst)]


    out_rngs = []

    for (st, end) in cur_rng_lst:
        out_rngs.extend(transform1range(mymap, st, end))

    return out_rngs



def transform1range(mymap, st, end):

    out = []

    previous = 1
    for (idx_deb, idx_fin, offset) in mymap:

        new_range, new_st, new_end = apply1range(previous, idx_deb-1, 0, st, end)

        if new_range:
            out.append(new_range)

        if new_end == None:
            break

        st = new_st
        end = new_end

        new_range, new_st, new_end = apply1range(idx_deb, idx_fin, offset, st, end)

        if new_range:
            out.append(new_range)

        if new_end == None:
            break

        st = new_st
        end = new_end

        previous = idx_fin+1


    if new_end != None:
        out.append((st, end))

    return out




def apply1range(idx_deb, idx_fin, offset, st, end):

    if not (idx_deb <= st <= idx_fin):
        return None, st, end

    if end <= idx_fin:
        until = end
        suite = None
    else:
        until = idx_fin
        suite = idx_fin+1

    st_off = st+offset
    end_off = until+offset

    if not suite:
        new_st = None
        new_end = None
    else:
        new_st = suite
        new_end = end

    return (st_off, end_off), new_st, new_end



print(f"{seeds=}")
locations = seedToLoc(sseeds)
print(f"{locations=}")


res = min(locations)

if not part2:
    print ("Valeur partie 1:", res[0])
    print ("Partie2 désactivée")

else:
    print ("Partie1 désactivée")
    print ("Valeur partie 2:", res[0])
