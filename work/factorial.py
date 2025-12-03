import sys
sys.set_int_max_str_digits(100000000)

def fact(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

print(len(str(fact(87655))))
