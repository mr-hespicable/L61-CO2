def zeckendorf_representation(n: int) -> list[int]:
    if not n or n <= 0:
        return []
    data = [0, 1]

    while data[-2] + data[-1] < n:
        data.append(data[-2] + data[-1])

    res: list[int] = []

    for i in reversed(range(len(data))):
        d = data[i]
        while n >= d and d != 0:
            n -= d
            res.append(d)

    return res


x = zeckendorf_representation(91239)
print(x)
