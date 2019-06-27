a = [6, -3, -2, 7, -15, 1, 2, 2]


def findSum(arr: list):
    if not arr:
        return 0
    dp = [0] * len(arr)
    dp[0] = arr[0]
    maxs = dp[0]
    for i in range(1,len(arr)):
        num = max(dp[i - 1] + arr[i], arr[i])
        dp[i] = num
        if dp[i] > maxs:
            maxs = dp[i]
    return maxs

print(findSum(a))