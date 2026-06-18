def fib(n):
    # return nth fibonacci number
    c = [1, 2]
    if n == 1:
        return c[0]
    elif n == 2:
        return c[1]

    for _ in range(n-2):
        c.append(sum(c))
        c.pop(0)
    return c[1]

latest = 0
n = 1
s = []
while latest < 4000000:
    s.append(latest)
    latest = fib(n)
    n += 1

print(sum([e for e in s if e % 2 == 0]))

