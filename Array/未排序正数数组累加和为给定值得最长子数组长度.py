def getMaxLength(arr: list, k: int) -> int:
    if not arr or k <= 0:
        return 0
    left, right = 0, 0
    sums = arr[0]
    lens = 0
    while right < len(arr):
        if sums == k:
            lens = max(lens, right - left + 1)
            sums -= arr[left]
            left += 1
        elif sums < k:
            right += 1
            if right == len(arr):
                break
            sums += arr[right]
        else:
            sums -= arr[left]
            left += 1
    return lens
print(getMaxLength([1, 2, 1, 1, 1],3))