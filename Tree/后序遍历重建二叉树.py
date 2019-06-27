from Tree import Tree


def posArrayToBST(posArr: list):
    if not posArr:
        return None
    posToBST(posArr, 0, len(posArr) - 1)


def posToBST(posArr, start, end):
    if start > end:
        return None
    head = Tree(posArr[end])
    less = -1
    more = end
    for i in range(start, end):
        if posArr[start] < posArr[end]:
            less = i
        else:
            more = i if more == end else more

    head.left = posToBST(posArr, start, less)
    head.right = posToBST(posArr, more, end - 1)
    return head
