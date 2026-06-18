a = {200: 99, 250: 104, 100: 999, 67: 999}
sorted_keys = {k: a[k] for k in sorted(a)}
sorted_values = dict(sorted(a.items(), key=lambda item: item[1]))

print(sorted_keys)
print(sorted_values)
