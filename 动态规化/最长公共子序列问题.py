import numpy


def getdp(str1: str, str2: str) -> list:
    dp = numpy.zeros((len(str1), len(str2)))
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    for i in range(1, len(str1)):
        dp[i][0] = max(dp[i - 1][0], 1 if str1[i] == str2[0] else 0)
    for j in range(1, len(str2)):
        dp[0][j] = max(dp[0][j - 1], 1 if str1[0] == str2[j] else 0)
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp


def lcse(str1: str, str2: str) -> str:
    if not str1 or not str2:
        return ''
    dp = getdp(str1, str2)
    m, n = len(str1) - 1, len(str2) - 1
    res = [''] * int(dp[m][n])
    idx = len(res) - 1
    while idx >= 0:
        if n > 0 and dp[m][n] == dp[m][n - 1]:
            n -= 1
        elif m > 0 and dp[m][n] == dp[m - 1][n]:
            m -= 1
        else:
            res[idx] = str1[m]
            idx -= 1
            m -= 1
            n -= 1
    return ''.join(res)

a = lcse('A1B2', 'AB3C4')
print(a)