def bucket(num, lens, mins, maxs) -> int:
    return ((num - mins) * lens) // (maxs - mins)


def maxGap(nums: list) -> int:
    if not nums or len(nums) < 2:
        return 0

    lens = len(nums)
    maxs = float('-inf')
    mins = float('inf')
    for i in nums:
        mins = min(i, mins)
        maxs = max(i, maxs)
    if maxs == mins:
        return 0
    hasNum: [bool] = [None] * (lens + 1)
    maxn: [int] = [0] * (lens + 1)
    minn: [int] = [0] * (lens + 1)
    for i in nums:
        bid = bucket(i, lens, mins, maxs)
        # print(bid)
        minn[bid] = min(minn[bid], i) if hasNum[bid] else i
        maxn[bid] = max(maxn[bid], i) if hasNum[bid] else i
        hasNum[bid] = True
    res = 0
    lastMax = 0
    i = 0
    while i <= lens:
        if hasNum[i]:
            lastMax = maxn[i - 1]
            break
        i += 1

    while i <= lens:
        if hasNum[i]:
            res = max(res, minn[i] - lastMax)
            lastMax = maxn[i]
        i += 1
    return res


print(maxGap([5, 2, 8, 20, 30]))