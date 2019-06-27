def main(matrix: list):
    tr = 0
    tc = 0
    endc = len(matrix[0]) - 1
    endr = len(matrix) - 1

    while tr != endr + 1:
        printLevel(matrix, tr, tc, endr)
        tr = tr + 1 if tc == endc else tr
        tc = tc if tc == endc else tc + 1



def printLevel(matrix:list, tr:int, tc:int, endr):
    while tc >= 0 and tr <= endr:
        print(matrix[tr][tc], end=' ')
        tc -= 1
        tr += 1

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
main(a)