in_string = input("Please enter text to compress: ") + " "

run_length_encoded = ""
current = ""
count = 1
for i in range(len(in_string) - 1):
    if not current:
        current = in_string[i]

    if current == in_string[i+1]:
        count += 1 

    else:
        run_length_encoded += f"{current} {count} "
        current = ""
        count = 1

print(run_length_encoded.strip())
