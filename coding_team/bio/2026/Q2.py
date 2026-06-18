def gen_cards(n, c, s):
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # n is number of letters
    # c is how many cards moved to bottom
    # s is how many times process is done
    
    sd = ''.join([2*alph[i] for i in range(n)])
    nd = sd
    print(len(nd))
    l1 = []
    l2 = []
    
    d1 = nd[:len(nd)//2]
    d2 = nd[len(nd)//2:]    
    print(n, c, s)
    for _ in range(s):
        d3 = list(''.join([''.join(t) for t in zip(d2, d1)])) # joined DADAetc
        if c > 0:
            g = ''.join(d3.copy()[:c]) # letters to the c-1th index
            print(g)
            print(d3)
            for _ in range(c):
                try:
                    d3.pop(0) # rm letters
                except:
                    continue
            d3 += g
        
        nd = d3
            
        d1 = nd[:len(nd)//2]
        d2 = nd[len(nd)//2:] 
            
    for _ in range(len(nd)):
        if type(nd) is not list:
            nd = list(nd)
        if nd[0] not in l1:
            l1.append(nd.pop(0))
        else:
            l2.append(nd.pop(0))
    
    return l1, l2

def cycle(ls1, n):
    for _ in range(n):
        ls1.append(ls1.pop(0))
    return ls1

def manip(alpha, beta):
    a = alpha
    la = len(a)
    b = beta
    lb = len(b)

    
    # manip alpha
    c2 = a.pop(1)
    ins = la//2
    a.insert(ins, c2)
    
    # manip beta
    b = cycle(b, 1)
    c3 = b.pop(2)
    ins = lb//2
    b.insert(ins, c3)
    
    return a, b

def encrypt(l1, l2, l):
    # one letter only
    a = l1
    b = l2
    
    movv = a.index(l)
    a = cycle(a, movv)
    b = cycle(b, movv)
    
    nl = b[0]
    a, b = manip(a, b)
    
    return a, b, nl

# main program

# n, s, c, stt = input().split()

def test(n, s, c, stt):
    n = int(n)
    s = int(s)
    c = int(c)

    # AAF F G G H H I I J JBBCCDDEE
    # F F G G H H I I J J

    alp, bet = gen_cards(n, c, s)

    ns = ''
    for ch in stt:
        alp, bet, nl = encrypt(alp, bet, ch)
        ns += nl
        
    return ns

# assert test(6, 3, 2, "BB") == "BD"
# assert test(26, 0, 0, "M") == "M"
# assert test(26, 2, 0, "P") == "W"
# assert test(26, 1, 1, "R") == "E"
# assert test(5, 10, 10, "CAB") == "CBE"
assert test(6, 10, 10, "FADE") == "ABFF"
print()
print()
print()
# assert test(9, 30, 2, "ABCDE") == "AHICD"
print(test(10, 30, 26, "BADGE"))
# assert test(19, 2026, 3, "GARDNER") == "NJFRAEG"
# assert test(26, 5000, 51, "SQUEAMISH") == "MXBMVODHN"
# assert test(20, 1000, 4, "OSSIFRAGE") == "DBOLRACBT"
