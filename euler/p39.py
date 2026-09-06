def triangle_sides(per: int):
    # per is the perimeter
    # function will return all possible side lengths for a perimeter

    tups = []
    
    for a in range(1, per-1):
        for b in range(1, a):
            c = per - (a + b)

            if a**2 + b**2 == c**2:

                tups.append((a, b, c))

    return tups

g = triangle_sides(840)

k = 0
sols = 0
for i in range(3, 1001):
    m = sols
    sols = max(sols, len(triangle_sides(i)))
    if m != sols:
        k = i


print(k)
