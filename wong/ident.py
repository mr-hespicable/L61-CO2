secure_id = input()

condition = (
    len(secure_id) == 9
    and secure_id[:2].isupper()
    and all([vowel not in secure_id[2:7].upper() for vowel in "AEIOU"])
    and sum(list(map(int, secure_id[7:]))) % 2 == 0
    if secure_id[7:].isnumeric()
    else False
)
if condition:
    print("VALID")
else:
    print("INVALID")
