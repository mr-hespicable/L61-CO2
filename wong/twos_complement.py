def convert_to_binary(val: int, num_bits: int) -> str:
    out: str = ""
    while val != 0:
        # print(val)
        r = str(val % 2)
        out = r + out
        val //= 2
    out = "0"*(num_bits-len(out)) + out
    return out


def convert_to_signed_binary(val: int, num_bits: int = 8) -> str:
    lower_limit: int = -1 * 2**(num_bits-1)
    upper_limit: int = 2**(num_bits-1)

    if not lower_limit <= val < upper_limit:
        raise ValueError(f"{val} cannot be represented in {num_bits} bits")

    unsigned_binary: str = convert_to_binary(abs(val), num_bits)
    print(f"unsigned_binary: {unsigned_binary}")
    signed_binary: str = "" 
    
    if val < 0:
        out = ""
        one = False
        for c in unsigned_binary[::-1]:
            if not one and c == "1":
                one = True
            else:
                c = "0" if c == "1" else "1"
            out = c + out

    return signed_binary


# Test your code here
print(convert_to_signed_binary(-128))
print(convert_to_signed_binary(127, 8))
print(convert_to_signed_binary(-30, 6))
print(convert_to_signed_binary(30, 6))
