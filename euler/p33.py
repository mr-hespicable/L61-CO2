from pprint import pprint

fracs = []

for i in range(10, 100):
    for j in range(10, 100):
        a, b = list(str(i))
        c, d = list(str(j))
        
        if int(d) != 0 and b == c and i/j == int(a) / int(d):
            fracs.append((i, j))

pprint(fracs)
