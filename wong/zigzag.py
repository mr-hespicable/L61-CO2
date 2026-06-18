plaintext = input("Give me some plaintext to encrypt: ")
num_rows = int(input())

filtered_plaintext = ""
for char in plaintext:
    if char.isalpha():
        filtered_plaintext += char

if num_rows not in [2, 3]:
    print("Invalid row selection")

else:
    seps = [2*n + 1 for n in range(num_rows-1)]
    seps = list(reversed(seps[1:])) + seps

    if len(seps) == 1:
        seps = 2*seps

    c = 0
    encrypted_text = ""
    for s in seps:
        encrypted_text += filtered_plaintext[c::s+1]
        c+=1

    print(encrypted_text)
