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

def squares_le(n: int):
    return [i**2 for i in range(1, int(n**0.5)+1)]

goal = 1000000

primes = primes_to_n(goal)

for i in range(3, goal + 1, 2):
    if i not in set(primes):
        if all(i - 2 * square not in set(primes) for square in squares_le(i)):
            print(i)
            break
