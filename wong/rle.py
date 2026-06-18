try:
    height = int(input())
    width = int(input())

    rows = []
    for _ in range(height):
        new_row = input()
        if len(new_row) != width:
            print("Invalid row length")
            break
        rows.append(new_row)

    if len(rows) == height:
        long = ''.join(rows) + " "
        c = 1
        rle_encoded = ""
        for i in range(1, len(long)):
            if long[i] == long[i-1]:
                c += 1
            else:
                rle_encoded += str(c) + long[i-1] + " "
                c = 1

        print(rle_encoded.strip())
except Exception:
    pass
