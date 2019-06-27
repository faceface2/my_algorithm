def heapAdjust(arr: list, parent: int, length: int) -> None:
    temp = arr[parent]
    child = 2 * parent + 1
    while child < length:
        while child + 1 < length and arr[child] > arr[child + 1]:
            child += 1
        if temp <= arr[child]:
            break
        arr[parent] = arr[child]
        parent = child
        child = child * 2 + 1
    arr[parent] = temp


def main():
    # arr = [int(i) for i in input().split()]
    #
    # m = int(input())
    arr = [8, 5, 10, 24, 86, 17]
    m = 4
    res = arr[:m]
    for i in range(m // 2, -1, -1):
        heapAdjust(res, i, m)

    print(res)
    for j in arr[m:]:
        if j > res[0]:
            res[0] = j
            heapAdjust(res, 0, m)
    print(res)


main()
