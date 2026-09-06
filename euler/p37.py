def truncatables(n: int):
    s = str(n)
    return sorted([int(s[i:]) for i in range(1, len(s))] + [int(s[:i+1]) for i in range(len(s)-1)])



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


primes = primes_to_n(1000000)
truncs = []

for prime in primes[4:]:
    if (
            not any(str(disallowed) in str(prime) for disallowed in [0, 4, 6, 8]) and
            all(k in primes for k in truncatables(prime))
            ):
        truncs.append(prime)


print(sum(truncs))
