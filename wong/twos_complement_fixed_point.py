def fixed_point(n: float):
    b_integer, b_fractional = str(n).split('.')
    integer = sum([2**int(i) for i in range(len(b_integer)) if b_integer[i] == "1"])
    fractional = sum([1/(2**int(i)) for i in range(len(b_integer)) if b_integer[i] == "1"])

fixed_point(101.111)
# integer = 5
# fraction = 0.875
