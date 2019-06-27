from Tree import Tree


def isbalance(head: Tree):
    res = [True]
    getHeight(head, 1, res)
    return res[0]


def getHeight(head: Tree, level: int, res: list):
    if not head:
        return level
    lh = getHeight(head.left, level + 1, res)
    if not res[0]:
        return level
    rh = getHeight(head.right, level + 1, res)
    if not res[0]:
        return level

    if abs(lh - rh) > 1:
        res[0] = False
    return max(lh, rh)
