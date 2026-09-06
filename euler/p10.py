import math

NUM = 2000000

d = [True for _ in range(NUM)]
print(len(d))

for i in range(2, math.isqrt(NUM)+1):
    if d[i]:
        for j in range(i**2, NUM, i):
            d[j] = False
    
print(sum([i for i in range(2, len(d)) if d[i]]))
