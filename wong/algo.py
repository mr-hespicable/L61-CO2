print("q1")
def Q1(x):
    answer = True
    for count in range(2, x):
        remainder = x % count
        if remainder == 0:
            answer = False
        print(answer, count, remainder)

Q1(7)
print("\nq2")

def Q2(lst: list[int]):
    ptr = 0
    temp = -1
    print(ptr, temp, lst)
    while ptr < 9:
        if lst[ptr] > lst[ptr+1]:
            temp = lst[ptr]
            lst[ptr] = lst[ptr+1]
            lst[ptr+1] = temp
        ptr += 1
        print(ptr, temp, lst)

Q2([43, 25, 37, 81, 18, 70, 64, 96, 52, 4])

List = [1234, 1789, 3125, 4789, 5006, 5789, 6502, 7411, 8407, 8971, 9053]

M = None

print("\nq3")
def X(E, L, H):
    global M
    print(E, L, H, M)
    if L > H:
        print(False)
    else:
        M = (L+H)//2
        if E == List[M-1]:
            print(True)
        else:
            if E < List[M-1]:
                X(E,L,M-1)
            else:
                X(E,M+1,H)


X(6502, 1, 11)

print("\nq4")
def Q4(lst):
    result = 0
    index = 0


    while index != 4:
        print(result, index)
        index += 1
        if result < lst[index-1]:
            result = lst[index-1]

    print(result, index)

Q4([24, 13, 57, 45])
