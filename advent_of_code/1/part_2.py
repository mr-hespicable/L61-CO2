f = open("input", "r")

d = 50
c = 0

for turn in f.readlines():
    dr = turn[0]
    num = int(turn[1:])

    for i in range(num):

        if dr == "L":
            d -= 1

        elif dr == "R":
            d += 1
            
        if d == 0:
            c += 1

        if d < 0:
            d = 99

        elif d > 99:
            d = 0
            c += 1

print(c)
