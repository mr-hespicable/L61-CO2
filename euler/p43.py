import itertools

def pandigitals():
    return list(map(lambda x: ''.join(x), list(itertools.permutations('0123456789', 10))))[362880:]

all_pans = pandigitals()
special_pans = []


for n in all_pans:
    if (
            int(n[1:4]) % 2 == 0 and
            int(n[2:5]) % 3 == 0 and
            int(n[3:6]) % 5 == 0 and
            int(n[4:7]) % 7 == 0 and
            int(n[5:8]) % 11 == 0 and
            int(n[6:9]) % 13 == 0 and
            int(n[7:10]) % 17 == 0
            ):
        special_pans.append(n)

print(sum(map(int, special_pans))) 
