from functools import reduce

def factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0))))

def d(n):
    if n == 1:
        return 1
    return sum(factors(n)) - n

c = {}
s = set()
for i in range(1, 10001):
    if i == d(d(i)) and i != d(i):
        s.add(i)

print(sum(s))
