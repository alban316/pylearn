file = open("parts.txt", "r")

t = file.read()

file.close()

tt = t.split("\n")
#st = tt[:25]


def ccount(ddict, i):
    ddict.setdefault(i)
    if ddict[i] is None:
        ddict[i] = 0
    ddict[i] += 1

d = {}
map(lambda i: ccount(d, i), tt)

print d