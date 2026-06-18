def caesar(text: str, string_shift: str):
    try:
        shift = int(string_shift)
    except Exception as _:
        return "Invalid shift value"

    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((((ord(char) - 65) + shift) % 26) + 65)


        elif char.islower():
            encrypted_text += chr((((ord(char) - 97) + shift) % 26) + 97)
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Give me some plaintext to encrypt: ")
shift = input()

print(caesar(plaintext, shift))
