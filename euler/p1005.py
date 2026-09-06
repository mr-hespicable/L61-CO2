goal_num = 20


def primes_to_n(n):
    primes = [2]
    for i in range(3, n+1):
        if not any([i % k == 0 for k in primes]):
            primes.append(i)
    return primes


ALL_PRIMES = primes_to_n(goal_num)[::-1]

# number: list of some primes that add to the number. e.g. {7: [[5, 2]]}. This means that 
# when you get c[p] where p is a prime, you can add p, and the extents of p
c = {}

def e_def(k, v):
    if k in c:
        c[k] += v
    else:
        c[k] = v

def populate(goal: int, primes: list[int]):
    if goal in c:
        return c[goal]
    else:
        for i in range(len(primes)):
            p = primes[i] 
            rem = goal - p 

            
            if rem in primes:
                e_def(goal, [p, rem])
                print(goal, p, rem, c)

            elif rem >= 2:
                print(goal, p, rem, c)
                a = primes.copy()
                a.remove(p)
                if goal in primes:
                    a.remove(goal)

                e_def(goal, populate(rem, a))


populate(20, ALL_PRIMES)
print(c)
