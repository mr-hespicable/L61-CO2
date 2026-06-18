pq = {"A": 10, "B": 9, "C": 1000, "D": 23, "E": 384, "F": 4}

npq = dict(zip(list(pq.values()), list(pq.keys())))
print(npq[min(npq.keys())])

print(min(pq, key=pq.get))
