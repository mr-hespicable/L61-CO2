def primes_to_n(n: int):
    k = [0] * (n+1)

    for i in range(2, n+1):
        if k[i] == 0:
            for j in range(2 * i, n, i):
                k[j] += 1


    return k
    r = [i for i, v in enumerate(k) if v != 0]
    return r[2:]


goal = 1000000
primes = primes_to_n(goal)
for i in range(len(primes)):
    p = primes[i] 
    q = primes[i+1] 
    r = primes[i+2] 
    s = primes[i+3] 
    print(p)

    if p == q == r == s == 4:
        print(i, i+1, i+2, i+3)
        break

