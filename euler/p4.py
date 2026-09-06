LIST = [i * j for j in range(100, 1000) for i in range(100, 1000)]
LIST.sort()

def is_palindrome(s):
    if len(s) % 2 == 0:
        return s[:len(s)//2] == s[len(s)//2:][::-1]
    else:
        return s[:len(s)//2] == s[len(s)//2+1:][::-1]

print(is_palindrome("abcba"))

for n in LIST[::-1]:
    if is_palindrome(str(n)):
        print(n)
        exit()

