goal = 1000000

def primes_to_n(n: int):
    k = [True] * n
    
    for i in range(2, int(n**0.5)):
        if k[i]:
            j = i**2
            while j < n:
                k[j] = False
                j += i
    r = [i for i, v in enumerate(k) if v]
    return r[2:]

def circle(p):
    sp = str(p)
    
    if len(str(p)) == 1:
        yield sp
    else:

        o = sp[1:] + sp[0]
        yield o

        t = 0
        while o != str(p):
            t += 1
            o = o[1:] + o[0]
            yield o

ALL_PRIMES = primes_to_n(goal)

circular_primes = []
for p in ALL_PRIMES:
    circles = [int(k) for k in circle(p)]
    if all(int(prime) in ALL_PRIMES for prime in circles):
            circular_primes.extend(circles)

cc = list(set(circular_primes))
print(len(cc))
