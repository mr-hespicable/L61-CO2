import math

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    f = []
    while n % 2 == 0:
        f.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0 and is_prime(i):
            f.append(i)
            n //= i

    if n > 2:
        f.append(n)
    return f


fs = []
for i in range(20, 1, -1):
    p = prime_factors(i)
    print(p)
    for j in p:
        if p.count(j) > fs.count(j):
            print(j, p.count(j), fs.count(j))
            fs.append(j)
    print()

print(math.prod(fs))

