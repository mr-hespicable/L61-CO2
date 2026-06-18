import math

NUM = 600851475143
def alg(n) -> list[int]:
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0: 
            factors.append(i)
    return factors

print(max([g for g in alg(NUM) if len(alg(g)) == 1]) )
