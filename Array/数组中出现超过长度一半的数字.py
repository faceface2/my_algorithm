import collections
a = [1,2,2,3,4,2,2]
ct = collections.Counter(a)
c=ct.most_common(1)
print(c)


def printHalfMajor(arr: list):
    cand = 0
    times = 0
    for i in arr:
        if times == 0:
            cand = i
            times = 1
        elif i == cand:
            times += 1
        else:
            times -= 1

    times = 0
    for i in arr:
        if i == cand:
            times += 1
    if times > len(arr) // 2:
        print(cand)
    else:
        print('no such number.')


printHalfMajor([1, 2, 2, 3, 1, 1,1])
