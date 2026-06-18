f = open("input", "r")
total = 0

ids = map(lambda x: x.strip().split("-"), f.read().split(","))

meow = 0

for rng in ids:
    low = rng[0]
    up = rng[1]

    if len(low) % 2 == 1:
        low = str(10**(len(low)))

    if int(low) > int(up):
        continue

    low_t, low_b = low[:len(low)//2], low[len(low)//2:]

    a = 2 * low_t

    while int(2 * low_t) < int(up):
        a = 2 * low_t
        if int(a) > int(up):
            break
        if int(a) > int(low):
            meow += int(a)

        low_t = str(int(low_t) + 1)

print(meow)
