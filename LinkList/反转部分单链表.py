from DataStructure import Node, init_node, print_node


def reversePart(head: Node, froms: int, to: int) -> Node:
    len_list: int = 0
    node1: Node = head
    fpre: Node = None
    tpos: Node = None
    while node1:
        # 找到from的前一个节点和to的后一个节点
        len_list += 1
        fpre = node1 if len_list == froms - 1 else fpre
        tpos = node1 if len_list == to + 1 else tpos
        node1 = node1.nexts
    if froms > to or froms < 1 or to > len_list:
        return head
    node1 = fpre.nexts if fpre else head
    node2: Node = node1.nexts
    node1.nexts = tpos
    while node2 != tpos:
        # 调整from 到 to直接节点的方向
        nxt = node2.nexts
        node2.nexts = node1
        node1 = node2
        node2 = nxt
    if fpre:
        fpre.nexts = node1
        return head
    return node1
