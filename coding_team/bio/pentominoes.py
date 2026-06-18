def matcher(let: str):
    match let:
        case "F":
            return [(0, 1), (1, 0), (1, 1), (1, 2), (2, 2)]
        case "G":
            return [(2, 1), (1, 0), (1, 1), (1, 2), (0, 2)]
        case "I":
            return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        case "L":
            return [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)]
        case "J":
            return [(1, 0), (1, 1), (1, 2), (1, 3), (0, 0)]
        case "N":
            return [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]
        case "M":
            return [(1, 0), (1, 1), (1, 2), (0, 2), (0, 3)]
        case "P":
            return [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
        case "Q":
            return [(1, 0), (1, 1), (0, 1), (1, 2), (0, 2)]
        case "T":
            return [(0, 2), (1, 0), (1, 1), (1, 2), (2, 2)]
        case "U":
            return [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
        case "V":
            return [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
        case "W":
            return [(0, 2), (0, 1), (1, 1), (1, 0), (2, 0)]
        case "X":
            return [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
        case "Z":
            return [(2, 0), (1, 0), (1, 1), (1, 2), (0, 2)]
        case "S":
            return [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
        case "Y":
            return [(1, 0), (1, 1), (1, 2), (1, 3), (0, 2)]
        case "A":
            return [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2)]
        case _:
            raise


def wh(shape: list[tuple[int, int]]):
    x = [a[0] for a in shape]
    y = [a[1] for a in shape]

    width = max(x) - min(x) + 1
    height = max(y) - min(y) + 1

    return (width, height)


def move(x, y, shape: list[tuple[int, int]]) -> list[tuple[int, int]]:
    nshape = []
    for n in shape:
        nshape.append((n[0] + x, n[1] + y))

    return nshape


def valid(s1: list[tuple[int, int]], s2: list[tuple[int, int]]):
    flag = False
    for n in s1:
        for m in s2:
            if intersect(n, m):
                return False

            elif _valid(n, m):
                flag = True

    return flag


def intersect(n1: tuple[int, int], n2: tuple[int, int]):
    x1, y1 = n1
    x2, y2 = n2

    return x1 == x2 and y1 == y2


def rang(a, b):
    c, d = max(a, b), min(a, b)
    return c - d


def _valid(n1: tuple[int, int], n2: tuple[int, int]):
    x1, y1 = n1
    x2, y2 = n2

    return not (x1 == x2 and y1 == y2) and (
        (x1 == x2 and rang(y1, y2) == 1) or (y1 == y2 and rang(x1, x2) == 1)
    )


arst = input()
L1, L2 = map(matcher, (arst[0], arst[1]))  # two letters

w1, h1 = wh(L1)
w2, h2 = wh(L2)

B = []

count = 0
for x in range(0 - w2, w1 + w2):
    for y in range(0 - h2, h1 + h2):
        S1 = L1.copy()
        S2 = move(x, y, L2.copy())

        if valid(S1, S2):
            S1.extend(S2)
            #print(S1)
            B.append(S1)
            count += 1


def dedup(R: list[list[tuple[int, int]]]):
    b = []
    for n in R:
        x, y = (min([a[0] for a in n]), min([a[1] for a in n]))
        
        m = n
        if x < 0:
            m = move(-x, 0, m)
        if y < 0:
            m = move(0, -y, m)

        m.sort()
        if m not in b:
            b.append(m)

    return b

print(len(dedup(B)))
