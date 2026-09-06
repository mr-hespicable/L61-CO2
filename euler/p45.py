def penta(n):
    return int(n * (3 * n - 1) / 2)

def hexa(n):
    return int(n * (2 * n - 1))

MAX = 500000

pents = [penta(k) for k in range(1, MAX+1)]
hexs = set([hexa(k) for k in range(1, MAX+1)])

for n in pents:
    if n in hexs:
        print(n) 


