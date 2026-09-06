def palindrome(n: int):
    s = str(n)
    if len(s) % 2 == 1:
        h2 = s[:len(s)//2+1][::-1]
    else:
        h2 = s[:len(s)//2][::-1]

    h1 = s[len(s)//2:]
    return h1 == h2

def d2b(n: int):
    return int(str(bin(n))[2:])


nums = [i for i in range(1, 1000000) if palindrome(i) and palindrome(d2b(i))]
print(sum(nums))
