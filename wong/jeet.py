number = input("Please enter a number: ")

while not number.isnumeric():
    number = input("Please enter a number: ")


def alternating(num: int):
    number = list(map(int, list(num)))
    diffs = []

    for i in range(len(number) - 1):
        if number[i] < number[i+1]:
            diffs.append(1)
        elif number[i] == number[i+1]:
            diffs.append(0)
        else:
            diffs.append(-1)
    
    
    if 0 in diffs:
        return (False, [1])

    for j in range(len(diffs) - 1):
        if diffs[j] == 1 and diffs[j+1] != -1:
            return (False, diffs)
        elif diffs[j] == -1 and diffs[j+1] != 1:
            return (False, diffs)
    return (True, diffs)
    
a = alternating(number)
if not a[0]:
    if all([k == 1 for k in a[1]]) or all([k == -1 for k in a[1]]):
        print("Not Alternating")
    else:
        print("Partly Alternating")
else:
    print("Alternating")
