char = input()
if 97 <= ord(char) <= 122:
    print(chr(ord(char)-32))
else:
    print("not a valid lowercase character!")
