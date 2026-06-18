f = open("example.csv", "r")
csv_list = [[entry.strip() for entry in line.split(",")] for line in f.readlines() if line.strip(",") != "\n" ]

num_records = len(csv_list)

avg_age = sum([int(record[2]) for record in csv_list[1:]])/(num_records-1)
avg_height = sum([float(record[1]) for record in csv_list[1:]])/(num_records-1)

print(f"number of people: {num_records}")
print(f"number of fields: {len(csv_list[0])}")
print(f"avg height is {avg_height:.2f} cm")
print(f"avg age is {int(avg_age)} years")

g = open("meow.csv", "w")

rstring = "\n".join([",".join(line) for line in csv_list])

g.write(rstring)
