from typing import List


class HeapNode:

    def __init__(self, value: int, arrNum: int, index: int):
        self.value = value
        self.arrNum = arrNum
        self.index = index


def heapInsert(heap, idx):
    while idx != 0:
        parent: int = (idx - 1) // 2
        if heap[parent].value < heap[idx].value:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break


def heapify(heap: List[HeapNode], index: int, heapSize: int):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    while left < heapSize:
        if heap[left].value > heap[index].value:
            largest = left
        if right < heapSize and heap[right].value > heap[largest].value:
            largest = right
        if largest != index:
            heap[largest], heap[index] = heap[index], heap[largest]
        else:
            break
        index = largest
        left = index * 2 + 1
        right = index * 2 + 2


def printTopK(matrix: List[List], topK: int) -> None:
    heapSize = len(matrix)
    heap: List[HeapNode] = [None] * heapSize
    for i in range(heapSize):
        index = len(matrix[i]) - 1
        heap[i] = HeapNode(matrix[i][index], i, index)
        heapInsert(heap, i)
    print('Top {} : '.format(topK))
    for i in range(topK):
        if heapSize == 0:
            break
        print(heap[0].value, end=' ')
        if heap[0].index != 0:
            heap[0].index -= 1
            heap[0].value = matrix[heap[0].arrNum][heap[0].index]
        else:
            heapSize -= 1
            heap[0], heap[heapSize] = heap[heapSize], heap[0]
        heapify(heap, 0, heapSize)


printTopK([[1, 3, 5, 6], [2, 4, 9], [5, 6, 8]], 3)
