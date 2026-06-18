f = open("input", "r")

d = 50
c = 0

for turn in f.readlines():
    dr = turn[0]
    num = int(turn[1:])
    a = d

    match dr:
        case "L":
            d -= num

        case "R":
            d += num

    d %= 100

    if d == 0:
        c += 1

print(c)


