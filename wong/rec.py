def add_nums(numbers):
    if len(numbers) > 1:
        numbers[0] += add_nums(numbers[1:])
    print(numbers)
    print(numbers[0])
    return numbers[0]
marks = [3, 6, 2, 8]
total = add_nums(marks)
print("Total =", total)
