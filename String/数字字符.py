import functools
num = [0,1,2,3,4,5,6,7,8,9]
a = [1,0,0,0,0,0,0,0,0,0]

test1 = '01112223456789'

def cmp(x,y):
    if a[x] < a[y]:
        return -1
    elif a[x] > a[y]:
        return 1
    else:
        return 0

def main(test:str):
    for i in test:
        a[int(i)] += 1
    temp = sorted(num, key=functools.cmp_to_key(cmp))
    if temp[0] == 0:
        print(1, end='')
    else:
        print(temp[0], end='')
    j = 0
    while j < a[temp[0]]:
        print(temp[0],end='')
        j += 1
main(test1)