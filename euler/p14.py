c = {n: 0 for n in range(1, 1000000)}
for i in range(20):
    c[2**i] = i+1

def clz(n):
    count = 0
    num = n

    while c[num] == 0:
        count += 1

        if num % 2 == 0:
            num //= 2
        else:
            num = 3*num + 1

        if num >= 1000000 and num not in c:
            c[num] = 0
    
    count += c[num]
    c[n] = count
    return count
                        

for j in range(1, 1000000):
    clz(j)
print(max(c.keys(), key=c.get))
