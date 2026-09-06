import itertools

def primes_to_n(n: int):
    z = [0] * (n)
    
    for i in range(2, int(n**0.5)):
        for j in range(i, n, i):
            if j > i:
                z[j] = 1

    return [i for i, v in enumerate(z) if v == 0][2:]


primes = [p for p in primes_to_n(10_000) if len(str(p)) == 4]

for p in primes:
    perms: list[int] = [int(x) for x in list(set([''.join(k) for k in list(itertools.permutations(str(p), 4))])) if len(str(int(x))) == 4]

    prime_perms = [perm for perm in perms if perm in primes]
    
    differences = {k: (j, abs(k - j)) for k in prime_perms for j in prime_perms if k != j}
    
    if len(differences) >= 2:
        print(differences)
        #print(list(differences.values()))
        realdiffs = [k[1] for k in list(differences.values())]

        vals = [k for k in list(differences.values()) if realdiffs.count(k[1]) >= 2]
        if vals:
            print(vals)
