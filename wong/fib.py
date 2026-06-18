import time
import sys
from collections.abc import Callable

sys.setrecursionlimit(2**31-1)

def fibonacci_no_recursion(n: int) -> int:
    flist: list[int] = [0, 1]
    for _ in range(n-1):
        flist.append(sum(flist))
        _ = flist.pop(0)
    
    return flist[0]


#c = {0: 0, 1: 1}
def fib_recurse(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    #if n in c:
    #    return c[n]
    
    #c[n] = fib_recurse(n-1) + fib_recurse(n-2)
    return fib_recurse(n-1) + fib_recurse(n-2)



def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n-1)

    

def time_func(f: Callable[[int], float], n: int) -> list[float]:
    start_time = time.time()
    result = f(n)
    return [time.time()-start_time, result]

a = 10
print(time_func(fibonacci_no_recursion, a)[0] * 10**3)
print(time_func(fib_recurse, a)[0] * 10**3)
#print(time_func(fact, 1))
