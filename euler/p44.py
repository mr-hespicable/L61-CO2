def penta(n):
    return int((n * (3*n-1)) / 2)

def is_pentagonal(P):
    if P <= 0:
        return False

    n: float = (1 + (1 + 24 * P)**0.5)/6
    if n.is_integer():
        return True
    return False

pents = [penta(i) for i in range(1, 10001)]

for j in pents:
    for k in pents:
        if j <= k:
            break
        elif is_pentagonal(j+k) and is_pentagonal(j - k):
            print(j, k, abs(k - j))

