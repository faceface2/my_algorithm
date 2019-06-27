from typing import List


# 给定一个矩阵m，从左上角开始每次只能向右或向下走，
# 最终到达右下角位置，路径上的所有数字累加起来就是路径和

def minPathSum1(m: List[List[int]]) -> int:
    if not m or not m[0]:
        return 0
    row = len(m)
    col = len(m[0])
    dp = []
    for i in range(row):
        dp.append([0] * col)
    dp[0][0] = m[0][0]
    for i in range(1, row):
        dp[i][0] = dp[i - 1][0] + m[i][0]
    for j in range(1, col):
        dp[0][j] = dp[0][j - 1] + m[0][j]
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]
    return dp[row - 1][col - 1]


def minPathSum2(m: List[List[int]]) -> int:
    if not m or not m[0]:
        return 0
    more = max(len(m), len(m[0]))
    less = min(len(m), len(m[0]))
    rowmore = more == len(m)
    dp = [0] * less
    dp[0] = m[0][0]
    for i in range(1, less):
        dp[i] = dp[i - 1] + (m[0][i] if rowmore else m[i][0])
    for i in range(1, more):
        dp[0] = dp[0] + (m[i][0] if rowmore else m[0][i])
        for j in range(1, less):
            dp[j] = min(dp[j - 1], dp[j]) + (m[i][j] if rowmore else m[j][i])
    return dp[-1]


s = minPathSum2([[1, 2, 3], [4, 5, 6]])

print(s)

# 123    1   3   6
# 456    5   8   12
