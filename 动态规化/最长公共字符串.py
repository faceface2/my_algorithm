import numpy


def getdp(str1: str, str2: str) -> list:
    dp = numpy.zeros((len(str1), len(str2)))
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    for i in range(len(str1)):
        dp[i][0] = 1 if str1[i] == str2[0] else 0
    for j in range(len(str2)):
        dp[0][j] = 1 if str1[0] == str2[j] else 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return dp


def lcst(str1: str, str2: str) -> str:
    if not str1 or not str2:
        return ''
    dp = getdp(str1, str2)
    end, maxs = 0, 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if dp[i][j] > maxs:
                maxs = int(dp[i][j])
                end = i
    return str1[end - maxs + 1: end + 1]


def lcst2(str1: str, str2: str) -> str:
    if not str1 or not str2:
        return ''
    row = 0
    col = len(str2) - 1
    end, maxs = 0, 0

    while row < len(str1):
        i = row
        j = col
        lens = 0
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                lens = 0
            else:
                lens += 1

            if lens > maxs:
                end = i
                maxs = lens
            i += 1
            j += 1
        if col > 0:
            col -= 1
        else:
            row += 1
    return str1[end - maxs + 1: end + 1]


print(lcst2('abcde', 'bebcd'))
