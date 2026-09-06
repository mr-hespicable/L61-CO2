def factorial(n):
    if n == 0:
        return 1

    v = 1
    for i in range(2, n+1):
        v *= i
    return v


v = []
for i in range(3, factorial(9) * 8):
    if sum(list(map(factorial, map(int, list(str(i)))))) == i:
        v.append(i) 
print(sum(v))

