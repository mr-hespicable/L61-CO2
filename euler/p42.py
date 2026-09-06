triangles = [int(0.5 * n * (n+1)) for n in range(1, 21)]

with open("0042_words.txt", 'r') as f:
    words = [k.strip('"') for k in f.read().split(',')]
    values = [sum([ord(c) - 64 for c in word]) for word in words]

    c = 0
    for value in values:
        if value in triangles:
            c += 1

    print(c)
