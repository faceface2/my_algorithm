from typing import Dict
from DataStructure.Node import RandNode


# 通过一个map来存放副本节点，然后将副本节点的指针连接
def copy_list_with_rand(head: RandNode) -> RandNode:
    mp: Dict[RandNode, RandNode] = dict()
    curr: RandNode = head
    while curr:
        mp[curr] = RandNode(curr.value)
        curr = curr.nexts
    curr = head
    while curr:
        mp[curr].nexts = mp[curr.nexts]  # 某一个副本节点的next指针即是 链表中节点的next在副本中的节点
        mp[curr].rand = mp[curr.rand]
        curr = curr.nexts
    return mp[head]


# 1) 在每个节点后插入副本节点 如：1->1`->2->2`->3->3`
# 2) 调整副本节点的rand指针
# 3) 调整节点的next指针，分离副本链表
def copy_list_with_rand2(head: RandNode) -> (RandNode, None):
    if not head:
        return None
    curr: RandNode = head
    while curr:
        nxt = curr.nexts
        curr.nexts = RandNode(curr.value)
        curr.nexts.nexts = nxt
        curr = nxt
    curr = head
    #设置复制节点的rand指针
    while curr:
        nxt = curr.nexts.nexts
        curr_copy: RandNode = curr.nexts
        curr_copy.rand = curr.rand.nexts if curr.rand else None
        curr = nxt
    res: RandNode = head.nexts
    curr = head
    # 分拆
    while curr:
        nxt = curr.nexts.nexts
        curr_copy = curr.nexts
        curr.nexts = nxt
        curr_copy.nexts = nxt.nexts if nxt else None
        curr = nxt
    return res

