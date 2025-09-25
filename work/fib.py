import time
from collections.abc import Callable

def fibonacci_no_recursion(n: int) -> int:
    flist: list[int] = [0, 1]
    for _ in range(n-1):
        flist.append(sum(flist))
        _ = flist.pop(0)
    
    return flist[0]


c = {0: 0, 1: 1}
def fib_recurse(n: int) -> int:
    if n in c:
        return c[n]
    
    c[n] = fib_recurse(n-1) + fib_recurse(n-2)
    return c[n]


def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n-1)

    

def time_func(f: Callable[[int], float], n: int) -> list[float]:
    start_time = time.time()
    result = f(n)
    return [time.time()-start_time, result]

print(time_func(fibonacci_no_recursion, 4))
print(time_func(fib_recurse, 4))
print(time_func(fact, 1))
