f = open("input", "r")
total = 0

ids = map(lambda x: x.strip().split("-"), f.read().split(","))

meow = 0

for rng in ids:
    low = rng[0]
    up = rng[1]

    length_diff = (len(up) - len(low)) + 1

    for ln in range(length_diff):
        length = len(low) + ln

        for i in range(1, len(low)+1):
            mult = len(low) // i

            print("i:", i)
            print("mult:", mult)

            # num divides length 
            if (length) % mult == 0 and i != length:
                repeated = 
                print("low_s:", repeated)
                while int(low) <= int(mult * repeated) <= int(up):
                    a = repeated * mult
                    print("id is", a)

                    if int(a) > int(up):
                        break
                    if int(a) > int(low):
                        meow += int(a)

                    repeated = str(int(repeated) + 1)
                print()
        print()
        print()

print(meow)
