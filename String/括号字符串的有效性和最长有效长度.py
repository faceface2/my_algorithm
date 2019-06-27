def is_valid(string: str) -> bool:
    if not string:
        return False
    status = 0
    for i in string:
        if i != ')' and i != '(':
            return False
        if i == ')':
            status -= 1
            if status < 0:
                return False
        if i == '(':
            status += 1
    return status == 0


def maxLength(str1: str) -> int:
    if not str1:
        return 0

    dp = [0] * len(str1)
    res = 0
    for i in range(len(str1)):
        if str1[i] == ')':
            pre = i - dp[i - 1] - 1
            if pre >= 0 and str1[pre] == '(':
                dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre > 0 else 0)
        res = max(res, dp[i])
    return res

if __name__ == '__main__':
    print(is_valid('((()))'))

    print(maxLength('(())'))

# 34+(4+5)*7

# ["34',"+",]
