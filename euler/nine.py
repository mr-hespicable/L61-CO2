import math
# thru algebraic manip:
# a*b + 500_000 == 1000*a + 1000*b

for a in range(1000):
    for b in range(1000):
        if a * b + 500_000 == 1000*a + 1000*b and a > 0 and b > 0:
            print(a*b*math.isqrt(a**2 + b**2))
            exit()
