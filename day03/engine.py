import sys

res1 = 0
res2 = 0

lines = []
matrix = []

part2 = True

def cherche_nums(l, row):

    in_num = False

    deb = -1
    fin = -1

    nums = []

    for i,c in enumerate(l):
        if in_num:
            if c.isdigit():
                fin = i
            else:
                in_num = False
                nstr = l[deb:fin+1]
                print("conversion", nstr, deb, fin, row)
                n = int(nstr)
                nums.append((row,deb,fin,n))
        else:
            if c.isdigit():
                deb = i
                fin = i
                in_num = True

    return nums

def cherche_symb(l, row):
    syms = []
    for i,c in enumerate(l):
        if not part2:
            if c != '.' and not c.isdigit():
                syms.append((row,i,c,[]))
        else:
            if c == '*':
                syms.append((row,i,c,[]))
    return syms



row = 0

all_nums = []
all_syms = []

for line in sys.stdin:
    line = line.strip()

    # print(row, line)
    # assert line[-1] == '.'
    line = line + '.'
    # line.append('.')

    nums = cherche_nums(line, row)
    all_nums.extend(nums)
    print("nums trouvés", nums)

    syms = cherche_symb(line, row)
    all_syms.extend(syms)
    print("syms trouvés", syms)

    lines.append(line)
    row += 1


def valid(row, deb, fin, val, syms):
    for r in range(row-1,row+2):
        for c in range(deb-1,fin+2):
            if exists(syms, r, c, val):
                return True
    return False


def exists(syms, r, c, val):
    for (sr, sc, _, list_adj) in syms:
        if sr == r and sc == c:
            list_adj.append(val)
            return True
    return False



for (row,deb,fin,val) in all_nums:
    if valid(row,deb,fin,val,all_syms):
        res1 += val

print("all syms", all_syms)

print ("Valeur partie 1:", res1)


for (_,_,_,adj) in all_syms:
    assert len(adj) <= 2
    if len(adj) == 2:
        res2 += adj[0]*adj[1]


print ("Valeur partie 2:", res2)
