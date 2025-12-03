nth = int(input("please give me a number: "))

cache = {0: 0, 1: 1}
def fib(n: int):
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

fib(nth)
print(list(cache.values())[1:])
