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


print(zeckendorf_representation(100))
print(zeckendorf_representation(1))
print(zeckendorf_representation(832040))
print(zeckendorf_representation(4))
print(zeckendorf_representation(623))
print(zeckendorf_representation(12))
print(zeckendorf_representation(834629))
print(zeckendorf_representation(33))
print(zeckendorf_representation(2023))
print(zeckendorf_representation(5000))
print(zeckendorf_representation(514228))
