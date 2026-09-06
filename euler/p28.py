# 1
# (2lvl+1)**2 = a, then a + a-lvl + a-2lvl + a-3lvl = 4a - 6lvl
# lvl increment 1 each time. max lvl = size**2

def i(n):
    if n == 1:
        return 1

    return 4 * (2*n-1)**2 - 12*(n-1) 

top = 1001
print(sum([i(k) for k in range(1, (top+1)//2 + 1)]))
