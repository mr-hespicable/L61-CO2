import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
n = 1
while len(primes) < 10001:
    n += 1
    if is_prime(n):
        primes.append(n)

print(max(primes))
