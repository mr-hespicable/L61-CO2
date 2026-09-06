from functools import cache

@cache
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


s = ""
n = 1
while len(s) != 1000:
    n += 1
    s = str(fib(n))
print(n)
