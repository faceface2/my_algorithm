def getMinLength(arr: list) -> int:
    if not arr or len(arr) < 2:
        return 0
    mins = arr[-1]
    noMinIndex = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > mins:
            noMinIndex = i
        else:
            mins = min(mins, arr[i])
    if noMinIndex == -1:
        return 0
    maxs = arr[0]
    noMaxIndex = -1
    for i in range(1, len(arr)):
        if arr[i] < maxs:
            noMaxIndex = i
        else:
            maxs = max(maxs, arr[i])
    return noMaxIndex - noMinIndex + 1


print(getMinLength([1, 5, 3, 4, 2, 6, 7]))
