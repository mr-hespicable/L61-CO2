def is_palindrome(a: int) -> bool:
    a = str(a)
    
    if len(a) % 2 == 0:
        h1 = a[:len(a)//2]
        h2 = a[len(a)//2:]

    else:
        h1 = a[:len(a)//2 + 1]
        h2 = a[len(a)//2:]

    return h1 == h2[::-1]

def prev_pal(a: int) -> int:
    if is_palindrome(a):
        return a
    #968

    b = str(a)
    if len(b) % 2 == 0:
        h1 = b[:len(b)//2]
        return int(str(int(h1)-1) + str(int(h1)-1)[::-1])

    else:
        h1 = b[:len(b)//2 + 1]
        return int(str(int(h1)-1) + str(int(h1)-1)[::-1][1:])


def compute_sum(i: int) -> list[int]:
    nums = []

    if prev_pal(i) == i:
        nums.append(i) 
        return nums
    
    prevpal = prev_pal(i)
    diff = i - prevpal
    
    while not is_palindrome(diff):
        i = prev_pal(i)
        diff = i - prev_pal(i)
        print(i, prevpal, diff)
    
    nums.extend(compute_sum(diff))

    return nums

print(compute_sum(9610))
