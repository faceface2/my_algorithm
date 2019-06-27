def maxProduct(arr: list) -> float:
    if not arr:
        return 0
    maxs = arr[0]
    mins = arr[0]
    res = arr[0]
    for idx, i in enumerate(arr):
        if idx == 0: continue
        maxEnd = maxs * i
        minEnd = mins * i
        maxs = max(max(maxEnd, minEnd), i)
        mins = min(min(maxEnd, minEnd), i)
        res = max(res, maxs)
    return res
