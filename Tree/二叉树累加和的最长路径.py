from Tree import Tree


def getMaxLength(head: Tree, sums: int):
    sum_map = {}
    sum_map[0] = 0
    return preOrder(head, sums, 0, 1, 0, sum_map)


def preOrder(head: Tree, sums: int, preSum: int, level: int, maxLen: int, sum_map: dict) -> int:
    if not head:
        return maxLen
    curSum = preSum + head.value
    if curSum not in sum_map:
        sum_map[curSum] = level
    if (curSum - sums) in sum_map:
        maxLen = max(level - sum_map.get(curSum - sums), maxLen)

    maxLen = preOrder(head.left, sums, curSum, level + 1, maxLen, sum_map)
    maxLen = preOrder(head.right, sums, curSum, level + 1, maxLen, sum_map)
    if level == sum_map.get(curSum):
        sum_map.pop(curSum)
    return maxLen


if __name__ == '__main__':
    a = Tree(-3)
    b = Tree(9)
    c = Tree(-9)
    d = Tree(1)
    e = Tree(-6)
    f = Tree(2)
    g = Tree(1)
    h = Tree(1)
    k = Tree(6)
    a.left = None
    a.right = c
    b.left= d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = k
    qq = getMaxLength(a, -9)
    print(qq)