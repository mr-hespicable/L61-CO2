import math

lmap: list[list[int]] = [[] for i in range(5)]
c = 0
for i in range(65, 90):
    lmap[int(math.floor(4-c//5))].append(chr(i))
    c += 1
    
def coord(string, n):
    # n is prev length, m is curr length.
    # for string=full string, n = m.
    size = 5**n
    letter = string[len(string) - n]
    
    i = 4 - ((ord(letter) - 65)//5)
    j = (ord(letter)-65)%5
    
    off_i = i * 5**(n-1)
    off_j = j * 5**(n-1)
        
    if n-1 == 0:
        return off_j, off_i

    else:
        gh = coord(string, n-1)
        off_j += gh[0]
        off_i += gh[1]
        return off_j, off_i    
    

l = list(input())

x, y = coord(l, len(l))
print(x+1, y+1)
