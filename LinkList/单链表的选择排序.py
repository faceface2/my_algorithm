from DataStructure.Node import Node


def section_sort(head: Node) -> Node:
    """
    每一轮循环找寻最小值节点，插入到已排序节点的尾部，
    并从原为排序链表中删除该节点，时间复杂度O(n2) 空间复杂度O(1)
    :param head:
    :return:
    """
    tail: Node = None
    curr = head
    while curr:
        small: Node = curr
        small_pre = get_smallest_pre_node(curr)
        if small_pre:
            small = small_pre.nexts
            small_pre.nexts = small.nexts
        curr = curr.nexts if small == curr else curr
        if tail:
            tail.nexts = small
        else:
            head = small
    return head


def get_smallest_pre_node(head: Node) -> Node:
    small_pre = None
    small = head
    curr = head.nexts
    pre = head
    while curr:
        if curr.value < small.value:
            small_pre = pre
            small = curr
        pre = curr
        curr = curr.next
    return small_pre
