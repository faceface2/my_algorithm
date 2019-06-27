from typing import List, Dict


class Node:
    left: 'Node' = None
    right: 'Node' = None

    def __init__(self, data):
        self.value = data

    def __repr__(self):
        return '<Node: {}>'.format(self.value)


StackNode = List[Node]
MapNode = Dict[Node, Node]


def main(arr: List[int]) -> Node:
    node_arr: List[Node] = []
    for i in arr:
        node_arr.append(Node(i))
    stack: StackNode = []
    l_big_map: MapNode = {}
    r_big_map: MapNode = {}

    # 找到每个数左边比它大的第一个数
    for node in node_arr:
        while stack and stack[-1].value < node.value:
            pop_stack_set_map(stack, l_big_map)
        stack.append(node)
    while stack:
        pop_stack_set_map(stack, l_big_map)

    # 找到每个数右边比它大的第一个数
    for node in reversed(node_arr):
        while stack and stack[-1].value < node.value:
            pop_stack_set_map(stack, r_big_map)
        stack.append(node)
    while stack:
        pop_stack_set_map(stack, r_big_map)

    head: Node = None
    for curNode in node_arr:
        left = l_big_map[curNode]
        right = r_big_map[curNode]
        if not left and not right:  # 如果左右两边没有比当前节点大的，则作为根节点
            head = curNode
        elif not left:  # 如果左边没有比当前节点大的，将当前节点作为右边比它的节点的左子树或右子树
            if not right.left:
                right.left = curNode
            else:
                right.right = curNode
        elif not right:
            if not left.left:
                left.left = curNode
            else:
                left.right = curNode
        else:
            parent = left if left.value < right.value else right  # 若左右两边都存在，则选取值比较小的作为parent
            if not parent.left:
                parent.left = curNode
            else:
                parent.right = curNode
    return head


def pop_stack_set_map(stack: StackNode, map_node: MapNode):
    popNode = stack.pop()
    if stack:
        map_node[popNode] = stack[-1]
    else:
        map_node[popNode] = None


def function(root):
    result = []
    if not root:
        return result
    A = []
    A.append(root)
    while A:
        temp = []
        size = len(A)
        for Node in A:
            temp.append(Node.value)
        result.append(temp)
        for i in range(size):
            node = A.pop(0)
            if node.left:
                A.append(node.left)
            if node.right:
                A.append(node.right)

    return result


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2]
    head = main(arr)
