import random
import time
from pprint import pprint
from collections import deque
from collections.abc import Callable


def merge_sort(unsorted_list: list[int]) -> list[int]:
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list)//2

    # .popleft() on a deque has 0(1) time complexity
    # vs .pop(0) on a list which has 0(n) time complexity
    left = deque(merge_sort(unsorted_list[:mid]))
    right = deque(merge_sort(unsorted_list[mid:]))

    rlist: list[int] = []
    while left and right:
        if left[0] < right[0]:
            rlist.append(left.popleft())
        else:
            rlist.append(right.popleft())

    rlist.extend(left or right)
    return rlist


def time_func(f: Callable[[list[int]], list[int]], n: list[int]) -> str:
    start_time = time.time()
    _result = f(n)
    return f"{f.__name__} took {time.time() - start_time} seconds; {_result}"


unsorted: list[int] = [random.randint(0, 1000000) for _ in range(400000)]
pprint(time_func(merge_sort, unsorted))
