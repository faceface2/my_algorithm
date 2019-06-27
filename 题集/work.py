import re


def func():
    matrix = input()
    string = input()
    if not matrix or len(matrix.strip()) != 3 or not matrix.replace(' ', '').isdigit():
        print('incorrect mesh size.')
        return
    row, col = [int(i) for i in matrix.split(' ')]
    c = '[GRF]+'
    matchobj = re.match(c, string).group()
    if matchobj != string:
        print('Incalid cell type')
        return
    if len(string) != row * col:
        print('Data mismatch')
        return
    flag = False
    count = 0
    i = 0
    while i < len(string):
        if not flag:
            print(string[i], end='')
            i += 1
            count += 1
            if count == col:
                flag = True
                print()
        else:
            print(string[i + count - 1], end='')
            count -= 1
            if count == 0:
                i += col
                flag = False
                print()


if __name__ == '__main__':
    func()

