import math

DIGITS = [i for i in range(10)]
facts = [math.factorial(i) for i in DIGITS][::-1]

def f():
    result = ""
    t = 999_999
     
    for i in range(10):
        index = t // facts[i]
        print(index)
        t %= facts[i] 

        digit = DIGITS.pop(index)
        result += str(digit) 
    return result

print(f())
