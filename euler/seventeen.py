# onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen is 106 chars

# twenty
# thirty
# fourty
# fifty
# sixty
# seventy
# eighty
# ninety
# one hundred
# two hundred
# three hundred
# four hundred
# five hundred
# six hundred
# seven hundred
# eight hundred
# nine hundred
# one thousand
# and

def makenstr(s):
    rrs = f"{s:03}"

    rs = "" 

    h = int(rrs[0])
    t = int(rrs[1])
    o = int(rrs[2])

    to = int(str(t) + str(o))
    toto = False

    match h:
        case 9:
            rs += "ninehundred"
        case 8:
            rs += "eighthundred"
        case 7:
            rs += "sevenhundred"
        case 6:
            rs += "sixhundred"
        case 5:
            rs += "fivehundred"
        case 4:
            rs += "fourhundred"
        case 3:
            rs += "threehundred"
        case 3:
            rs += "threehundred"
        case 2:
            rs += "twohundred"
        case 1:
            rs += "onehundred"
        case _:
            pass

    if h != 0 and (t > 0 or o > 0):
        rs += "and"

    match to:
        case 10:
            toto = True
            rs += "ten"
        case 11:
            toto = True
            rs += "eleven"
        case 12:
            toto = True
            rs += "twelve"
        case 13:
            toto = True
            rs += "thirteen"
        case 14:
            toto = True
            rs += "fourteen"
        case 15:
            toto = True
            rs += "fifteen"
        case 16:
            toto = True
            rs += "sixteen"
        case 17:
            toto = True
            rs += "seventeen"
        case 18:
            toto = True
            rs += "eighteen"
        case 19:
            toto = True
            rs += "nineteen"
        case _:
            pass

    match t:
        case 9:
            rs += "ninety"
        case 8:
            rs += "eighty"
        case 7:
            rs += "seventy"
        case 6:
            rs += "sixty"
        case 5:
            rs += "fifty"
        case 4:
            rs += "forty"
        case 3:
            rs += "thirty"
        case 2:
            rs += "twenty"
        case _:
            pass
    

    if not toto:
        match o:
            case 9:
                rs += "nine"
            case 8:
                rs += "eight"
            case 7:
                rs += "seven"
            case 6:
                rs += "six"
            case 5:
                rs += "five"
            case 4:
                rs += "four"
            case 3:
                rs += "three"
            case 2:
                rs += "two"
            case 1:
                rs += "one"
            case _:
                pass


    return rs

s = ""
for i in range(1, 1000):
    s += makenstr(i)
s += "onethousand"
print(len(s))
