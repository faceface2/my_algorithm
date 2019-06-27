def isPostArray(arr: list):
    if not arr:
        return False
    return isPost(arr, 0, len(arr) - 1)


def isPost(arr: list, start: int, end: int):
    if start == end:
        return True
    less = -1
    more = end
    for i in range(less, end):
        if arr[i] < arr[end]:
            less = i
        else:
            more = i if more == end else more
    if less == -1 or more == end:
        return isPost(arr, start, end - 1)
    if less != more - 1:
        return False
    return isPost(arr, start, less) and isPost(arr, more, end - 1)
