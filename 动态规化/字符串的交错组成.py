import numpy


def isCross1(str1: str, str2: str, aim: str) -> bool:
    if not str1 or not str2 or not aim:
        return False
    if len(str1) + len(str2) != len(aim):
        return False
    dp = numpy.zeros((len(str1) + 1, len(str2) + 1))
    dp[0][0] = True
    for i in range(1, len(str1) + 1):
        if str1[i - 1] != aim[i - 1]:
            break
        dp[i][0] = True
    for j in range(1, len(str2) + 1):
        if str2[j - 1] != aim[j - 1]:
            break
        dp[0][j] = True
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if (str1[i - 1] == aim[i + j - 1] and dp[i - 1][j]) or (str2[j - 1] == aim[i + j - 1] and dp[i][j - 1]):
                dp[i][j] = True
    print(dp)
    return dp[len(str1)][len(str2)]


print(isCross1('12', 'ab', 'a1b2'))
