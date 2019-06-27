from collections import deque
from typing import List, Deque


def main(arr: List[int], w: int) -> None:
    res: List[int] = list()
    qmax: Deque = deque()
    for i, num in enumerate(arr):
        while qmax and arr[qmax[-1]] < num:
            qmax.pop()
        qmax.append(i)
        if qmax[0] == i - w:
            qmax.popleft()
        if i >= w - 1:
            res.append(arr[qmax[0]])

    print(res)


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    main(arr, 3)
