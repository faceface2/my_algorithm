def get_next(ps: str):
    nexts = [None] * len(ps)
    nexts[0] = -1
    j = 0
    k = -1
    while j < len(ps) - 1:
        if k == -1 or ps[j] == ps[k]:
            j += 1
            k += 1
            nexts[j] = k
        else:
            k = nexts[k]
    return nexts


def KMP(ts, ps):
    i = 0  # 主串的位置
    j = 0  # 模式串的位置
    nexts = get_next(ps)
    while i < len(ts) and j < len(ps):
        if j == -1 or ts[i] == ps[j]:  # 当j为-1时，要移动的是i，当然j也要归0
            i += 1
            j += 1
        else:
            # i不需要回溯了
            j = nexts[j]  # j回到指定位置

    if j == len(ps):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    c = KMP('abcdabc', 'dab')
    print(c)
