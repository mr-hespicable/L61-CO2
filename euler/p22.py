def alph_value(s):
    return sum([ord(c) - 64 for c in s])

f = open("0022_names.txt")
g = [i.strip("\"") for i in f.read().split(",")]
g.sort()

s = 0
for i in range(len(g)):
    #print((i+1), g[i], alph_value(g[i]))
    s += (i+1) * alph_value(g[i])

print(s)

