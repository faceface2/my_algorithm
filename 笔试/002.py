from typing import List


def main():
    result: List[int] = [0] * (100000 // 100)
    with open('input2.txt', 'r') as f:
        while 1:
            try:
                num_s = f.readline()
                if not num_s:
                    break
                num = int(num_s)
            except ValueError:
                continue
            r = num // 100
            result[r] += 1
    for idx, i in enumerate(result, 0):
        p = '{}-{} {}'.format(idx * 100, (idx + 1) * 100 - 1, i)
        print(p)


main()
