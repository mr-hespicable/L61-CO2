g = ''.join([str(i) for i in range(1, 200000)])

p = 1
for i in range(7):
    print(g[10**i-1])
    p *= int(g[10**i-1])

print(p)
