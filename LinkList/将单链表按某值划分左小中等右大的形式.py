from typing import List
from DataStructure.Node import Node, init_node, print_node


def list_partition1(head: Node, pivot: int) -> Node:
    if not head:
        return head
    curr: Node = head
    arr = list()
    while curr:
        arr.append(curr)
        curr = curr.nexts
    arr_partition(arr, pivot)
    for i in range(1, len(arr)):
        arr[i - 1].nexts = arr[i]
    arr[-1].nexts = None
    return arr[0]


def arr_partition(nodeArr: List[Node], pivot: int) -> None:
    small = -1
    big = len(nodeArr)
    idx = 0
    while idx != big:
        if nodeArr[idx].value < pivot:
            small += 1
            nodeArr[small], nodeArr[idx] = nodeArr[idx], nodeArr[small]
            idx += 1
        elif nodeArr[idx].value == pivot:
            idx += 1
        else:
            big -= 1
            nodeArr[big], nodeArr[idx] = nodeArr[idx], nodeArr[big]


# 按照原先后顺序进行划分
# 将链表的所有节点依次划分进三个链表，然后再连接三个链表即可
def list_partition2(head: Node, pivot) -> Node:
    # 小链表的头尾指针
    sH: Node = None
    sT: Node = None
    # 等链表的头尾指针
    eH: Node = None
    eT: Node = None
    # 大链表的头尾指针
    bH: Node = None
    bT: Node = None
    while head:
        nt = head.nexts
        head.nexts = None
        if head.value < pivot:
            if sH:
                sT.nexts = head
                sT = head
            else:
                sH = head
                sT = head
        elif head.value == pivot:
            if eH:
                eT.nexts = head
                eT = head
            else:
                eH = head
                eT = head
        else:
            if bH:
                bT.nexts = head
                bT = head
            else:
                bH = head
                bT = head
        head = nt
    # 判断小链表和等链表是否存在
    if sT:
        sT.nexts = eH
        eT = eT if eT else sT
    if eT:
        eT.nexts = bH
    return sH if sH else eH if eH else bH


if __name__ == '__main__':
    arr = [3, 5, 1, 6, 9, 4, 8]
    head = init_node(arr)
    h = list_partition1(head, 5)
    h2 = list_partition2(head, 5)
    print_node(h)
    print_node(h2)
