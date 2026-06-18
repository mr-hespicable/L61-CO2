data = [["Alice James Paul", 123, 15], ["Bob", 456, 15], ["Chaz", 28, 9], ["Dave", 15, 121]]

name = ""
n1 = 0
n2 = 0

name_len = max([len(str(item[0])) for item in data]) + 1
n1_len = max([len(str(item[1])) for item in data]) + 1
n2_len = max([len(str(item[2])) for item in data]) + 1


for i in range(len(data)):
    name = data[i][0]
    n1 = data[i][1]
    n2 = data[i][2]


    print(f"+{'-' * (name_len+1)}+{'-' * (n1_len+1)}+{'-' * (n2_len+1)}+")
    print(f"| {name:<{name_len}}|{n1:>{n1_len}} |{n2:>{n2_len}} |")

print(f"+{'-' * (name_len+1)}+{'-' * (n1_len+1)}+{'-' * (n2_len+1)}+")
