s = 0
for i in range(2, 10**6):
    if i == sum(k**5 for k in list(map(int, list(str(i))))):
        s += i

print(s)
