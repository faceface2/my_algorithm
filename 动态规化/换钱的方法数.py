import numpy


def coins(arr: list, aim: int):
    if not arr or aim < 0:
        return 0
    s = process1(arr, 0, aim)
    return s


def process1(arr: list, index: int, aim: int) -> int:
    res = 0
    if index == len(arr):
        res = 1 if aim == 0 else 0
    else:
        i = 0
        while arr[index] * i <= aim:
            res += process1(arr, index + 1, aim - arr[index] * i)
            i += 1
    return res


def coins2(arr: list, aim: int):
    if not arr or aim < 0:
        return 0
    maps = numpy.zeros((len(arr) + 1, aim + 1))
    s = process1(arr, 0, aim, maps)
    return s


def process2(arr: list, index: int, aim: int, maps) -> int:
    res = 0
    if index == len(arr):
        res = 1 if aim == 0 else 0
    else:
        i = 0
        while arr[index] * i <= aim:
            mapValue = maps[index + 1][aim - arr[index] * i]
            if mapValue != 0:
                res += 0 if mapValue == -1 else mapValue
            else:
                res += process1(arr, index + 1, aim - arr[index] * i, maps)
            i += 1
    maps[index][aim] = -1 if res == 0 else res
    return res


def coins3(arr: list, aim: int):
    if not arr or aim < 0:
        return 0
    dp = numpy.zeros((len(arr), aim + 1))
    for i in range(len(arr)):
        dp[i][0] = 1
    j = 1
    while arr[0] * j <= aim:
        dp[0][arr[0] * j] = 1
        j += 1
    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            num = 0
            k = 0
            while j - arr[i] * k >= 0:
                num += dp[i - 1][j - arr[i] * k]
                k += 1
            dp[i][j] = num
    return dp[len(arr) - 1][aim]


def coins4(arr: list, aim: int):
    if not arr or aim < 0:
        return 0
    dp = numpy.zeros((len(arr), aim + 1))
    for i in range(len(arr)):
        dp[i][0] = 1
    j = 1
    while arr[0] * j <= aim:
        dp[0][arr[0] * j] = 1
        j += 1
    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i][j - arr[i]] if j - arr[i] >= 0 else 0
    return dp[len(arr) - 1][aim]


def coins5(arr: list, aim: int):
    if not arr or aim < 0:
        return 0
    dp = [0] * (aim + 1)
    j = 0
    while arr[0] * j <= aim:
        dp[arr[0] * j] = 1
        j += 1
    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[j] += dp[j - arr[i]] if j - arr[i] >= 0 else 0
    return dp[aim]


b = coins5([5, 10, 25, 1], 100)
print(b)
