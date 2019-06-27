def getLiL2(arr: list):
    if not arr:
        return 0
    lens = 0
    sets = set()
    for i in range(len(arr)):
        maxs = float('-inf')
        mins = float('inf')
        for j in range(i, len(arr)):
            if arr[j] in sets:
                break
            sets.add(arr[j])
            maxs = max(maxs, arr[j])
            mins = min(mins, arr[j])
            if maxs - mins == j - i:
                lens = max(lens, j - i + 1)
        sets.clear()
    return lens


print(getLiL2([3, 2, 4, 3, 5, 7]))

# 1 2 1 1 1