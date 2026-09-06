def prime_factors(n):
    f = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            f.append((i, n//i))
    f.sort()
    return f

def pandigital(a, b):
    g = ['1','2','3','4','5','6','7','8','9']
    for c in str(a) + str(b) + str(int(a) * int(b)):
        if c not in g:
            return False
        else:
            g.remove(c)
    if not g:
        return True
    else:
        return False


pandigitals = set({})
for i in range(10000):
    factors = prime_factors(i)

    for f1, f2 in factors:
        if pandigital(f1, f2):
            pandigitals.add(i)
print(sum(list(pandigitals))) 
