import random
from matplotlib import pyplot as plt

MAX = 2


def search(sorted_list: list[int], target: int):
    start = 0
    end = len(sorted_list) - 1
    mid_point = int((start + end) / 2)
    item = sorted_list[mid_point]

    while start <= end:
        mid_point = int((start + end) / 2)
        item = sorted_list[mid_point]

        if target < item:
            start = mid_point + 1

        elif target == item:
            return True

        else:  # target > item
            end = mid_point - 1

    return False


def gen_list(n, limit):
    return [random.randint(0, limit) for _ in range(n)]




x = []
y = []

for MAX in range(1, 100):
    data = list(sorted(gen_list(2000, MAX)))
    pps = []
    for i in range(50):
        falses = 0
        trues = 0
        for i in range(1000):
            if search(data, random.randint(0, MAX)):
                trues += 1
            else:
                falses += 1

        #print(trues)
        #print(falses)
        pps.append(100 * trues/falses)
    x.append(MAX)
    y.append(sum(pps)/len(pps))

plt.plot(x, y)
plt.show()
