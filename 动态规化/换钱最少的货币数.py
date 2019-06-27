import sys
from typing import List


def minCoins1(arr: List[int], aim: int):
    if not arr or aim < 0:
        return 0
    maxs = sys.maxsize
    n = len(arr)
    dp = []
    for i in range(n):
        dp.append([0] * (aim + 1))
    for j in range(1, aim + 1):
        dp[0][j] = maxs
        if j - arr[0] >= 0 and dp[0][j - arr[0]] != maxs:
            dp[0][j] = dp[0][j - arr[0]] + 1

    for i in range(1, n):
        for j in range(1, aim + 1):
            left = maxs
            if j - arr[i] >= 0 and dp[i][j - arr[i]] != maxs:
                left = dp[i][j - arr[i]] + 1
            dp[i][j] = min(left, dp[i - 1][j])
    return dp[n - 1][aim] if dp[n - 1][aim] != maxs else -1



def minCoins2(arr: List[int], aim: int):
    if not arr or aim < 0:
        return 0
    maxs = sys.maxsize
    n = len(arr)
    dp = [0]* (aim+1)

    for j in range(1, aim + 1):
        dp[j] = maxs
        if j - arr[0] >= 0 and dp[j - arr[0]] != maxs:
            dp[j] = dp[j - arr[0]] + 1

    for i in range(1, n):
        for j in range(1, aim + 1):
            left = maxs
            if j - arr[i] >= 0 and dp[j - arr[i]] != maxs:
                left = dp[j - arr[i]] + 1
            dp[j] = min(left, dp[j])
    return dp[aim] if dp[aim] != maxs else -1

print(minCoins2([2,5,3],8))