from math import log2, comb, floor
from collections import defaultdict

def num_moves(n):
    b = bin(n)[2:]
    return b.count('1') + len(b) - 1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    d = int(floor(log2(n)))

    for l in range(1, d+1):
        lens = l-1
        k

