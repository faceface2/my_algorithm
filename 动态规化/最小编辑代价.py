import numpy


def minCost1(str1: str, str2: str, ic: int, dc: int, rc: int) -> int:
    if not str1 or not str2:
        return 0
    row = len(str1) + 1
    col = len(str2) + 1
    dp = numpy.zeros((row, col))
    for i in range(row):
        dp[i][0] = dc * i
    for j in range(col):
        dp[0][j] = rc * j
    for i in range(1, row):
        for j in range(1, col):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + rc
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + ic)
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + dc)
    return dp[row - 1][col - 1]


print(minCost1('ab12cd3', 'abcdf', 5, 3, 2))
