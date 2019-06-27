def getLessIndex(arr: list) -> int:
    if not arr:
        return -1
    if len(arr) == 1 or arr[0] < arr[1]:
        return 0
    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return len(arr) - 1
    left = 1
    right = len(arr) - 2
    mid = 0
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid-1]:
            right = mid - 1
        elif arr[mid] > arr[mid+1]:
            left = mid + 1
        else:
            return mid

    return left