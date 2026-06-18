def convert(decimal: int, base: int = 2) -> str:
    n = decimal
    out_string = ""

    if n == 0:
        return "0"

    while n != 0:
        n = decimal // base
        if n >= 10:
            out_string = chr((decimal % base) + 55) + out_string
        else:
            out_string = str(decimal % base) + out_string
        decimal = n

    return out_string


print(convert(84, 17))
print(convert(35, 2))
print(convert(35, 10))
print(convert(35, 16))

