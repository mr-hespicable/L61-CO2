import math

def factors(n: int):
    f = set({})
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return f


l = 0
n = 0
t = 0
while l <= 500:
    n += 1
    t = sum([i for i in range(1, n+1)])
    l = len(factors(t))

print(l, n, t)
