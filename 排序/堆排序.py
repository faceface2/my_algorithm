import heapq


def headAdjust(arr: list, parent: int, length: int) -> None:
    temp = arr[parent]
    child = 2 * parent + 1
    while child < length:
        while child + 1 < length and arr[child] < arr[child + 1]:
            child += 1

        if temp >= arr[child]:
            break
        arr[parent] = arr[child]

        parent = child
        child = child * 2 + 1

    arr[parent] = temp


def heapsort():
    arr = [1, 3, 4, 5, 2, 6, 9, 7, 8, 0]
    for i in range(int(len(arr) / 2), -1, -1):
        headAdjust(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        headAdjust(arr, 0, i)

    print(arr)


heapsort()


