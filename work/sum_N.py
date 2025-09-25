import time
from collections.abc import Callable

def sum_N(n: int) -> float:
    s = sum([i for i in range(1, n+1)])
    return float(s)

def sum_N_gauss(n: int) -> float:
    s = 0.5*n*(n+1)
    return s


def pi_approx(n: int) -> float:
    total = 3
    if n <= 0:
        return 3
    for i in range(1, n+1):
        denom = 2*i * (2*i+1) * (2*i+2)
        if i % 2 == 1:
            total += 4/denom
        else:
            total -= 4/denom
    return total

def time_func(f: Callable[[int], float], n: int):
    start_time = time.time()
    result = f(n)
    return [time.time()-start_time, result]


def test(l: list[Callable[[int], float]], input: int):
    for func in l:
        time, out = time_func(func, input)
        yield f"{func.__name__} took {time} seconds and the output was {out}"


# test([sum_N, sum_N_gauss])
for result in test([sum_N, sum_N_gauss, pi_approx], 2000000):
    print(result)
