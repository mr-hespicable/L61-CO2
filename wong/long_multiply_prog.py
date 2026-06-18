def long_multiply(a: int, b: int) -> str:
    """
    This function assumes both `a` and `b` are correctly formatted
    binary numbers.
    """
    add_nums: list[str] = []

    # compute a * b
    for i, c in enumerate(reversed(str(b))):
        match int(c):
            case 0:
                add_nums.append("0" * (len(str(a)) + i))
            case 1:
                add_nums.append(str(a) + "0" * (i))

    for j in add_nums:
        print(j)
    return ""
        


_ = long_multiply(1101, 101)
