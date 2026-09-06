def pandigital(a):
    g = ['1','2','3','4','5','6','7','8','9']
    for c in str(a):
        if c not in g:
            return False
        else:
            g.remove(c)
    if not g:
        return True
    else:
        return False

def concat(integer: int, n: int):
    return int(''.join(map(str, [integer * i for i in range(1, n+1)])))

largest = 0

for i in range(1, 100000):
    for j in range(1, 10):
        n = concat(i, j)
        if len(str(n)) == 9 and pandigital(n):
            largest = max(largest, n)


print(largest)

