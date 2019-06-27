from .Node import Node
from typing import List

def reverseKNodes1(head: Node, k: int) -> Node:
    if k < 2:
        return head
    stack = list()
    new_head = head
    curr = head
    pre = None
    while curr:
        next_node = curr.next
        stack.append(curr)
        if len(stack) == k:
            pre = resignl(stack, pre, next_node)
            new_head = curr if new_head == head else new_head
        curr = next_node
    return new_head

def resignl(stack: List[Node], left: Node, right: Node)-> Node:
    curr = stack.pop()
    if left:
        left.next = curr
    while stack:
        next_node = stack.pop()
        curr.next = next_node
        curr = next_node
    curr.next = right
    return curr
