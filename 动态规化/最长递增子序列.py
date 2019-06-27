def getdp1(arr: list) -> list:
    dp = [0] * len(arr)
    for i in range(len(arr)):
        dp[i] = 1
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def generateLIS(arr: list, dp: list) -> int:
    length = 0
    index = 0
    for idx, i in enumerate(dp):
        if i > length:
            length = i
            index = idx
    lis = [0] * length
    length -= 1
    lis[length] = arr[index]
    for i in range(index, -1, -1):
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            length -= 1
            lis[length] = arr[i]
            index = i
    return lis


def lis1(arr: list):
    if not arr:
        return None
    dp = getdp1(arr)
    return generateLIS(arr, dp)


print(lis1([2, 1, 5, 3, 6, 4, 8, 9, 7]))
