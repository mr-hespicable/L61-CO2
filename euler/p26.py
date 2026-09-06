def longdiv(bottom: int):
    top = 1
    encountered = []
    done = False

    while top != 0 and not done:
        while top < bottom:
            encountered.append(0)
            top *= 10


        if top in encountered:
            done = True
            while encountered[0] != top:
                encountered.pop(0)
            return len(encountered)

        encountered.append(top)
        top %= bottom
        top *= 10

    return 0


k = {longdiv(i): i for i in range(1, 1000)}
print(k[max(k)])
