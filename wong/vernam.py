plaintext = input()
key = input()

if len(key) != len(plaintext):
    print("Invalid key length")

else:
    encrypted_nums = ""
    for c1, c2 in list(zip(plaintext, key)):
        encrypted_nums += str(ord(c1) ^ ord(c2)) + " "

    print(encrypted_nums.strip())
