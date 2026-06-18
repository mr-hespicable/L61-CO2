# part 1
with open("input", "r") as ins:
    l = 0
    sett = set({})
    for line in ins:
        print(line.strip())
        print(sett)
        if line == '\n':
            l += len(sett)
            print(l)
            sett = set({})
        else:
            for c in line.strip():
                sett.add(c)

    print(l)


# part 2 
with open("input_2", "r") as ins:
    sum_counts = 0
    sets: list[set] = []
    for line in ins:
        if line != "\n":
            sets.append(set(line.strip()))
        else:
            t = sets[0].intersection(*sets[1:])
            sets = []
            sum_counts += len(t)
    print(sum_counts)
