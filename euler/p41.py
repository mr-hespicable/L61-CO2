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

def maxpd(n):
    return int(''.join([str(i) for i in range(1, n+1)][::-1]))

def pandigital(a, n):
    g = [str(i) for i in range(1, n+1)]
    for c in str(a):
        if c not in g:
            return False
        else:
            g.remove(c)
    if not g:
        return True
    else:
        return False


largest = 0
for n in range(1, 8):
    primes = primes_to_n(maxpd(n))

    for i in range(len(primes)):
        p = primes[i]
        if len(str(p)) == n and pandigital(p, n):
            largest = max(largest, p)

print(largest)

