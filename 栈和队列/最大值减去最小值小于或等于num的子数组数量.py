from typing import List, Deque
from collections import deque


def get_num(arr: List, num: int):
    if not arr:
        return 0
    qmin: Deque = deque()
    qmax: Deque = deque()
    i: int = 0
    j: int = 0
    res: int = 0
    while i < len(arr):
        while j < len(arr):
            while qmin and arr[qmin[-1]] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            while qmax and arr[qmax[-1]] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmin[0] == i:
            qmin.popleft()
        if qmax[0] == i:
            qmax.popleft()
        res += j - i
        i += 1
    return res 

li = [3,5,7,10]
s = get_num(li, 3)
print(s)