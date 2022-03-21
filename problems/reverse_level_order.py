# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
#  i.e., the lowest level comes first. You should populate the values of all nodes in each level 
# from left to right in separate sub-arrays.

from collections import deque

class TreeNode:
    def __init__(self, value, right=None, left=None) -> None:
        self.value = value
        self.right = right
        self.left = left


def traverse(root):
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_nodes = []
        current_size = len(queue)

        for _ in range(current_size):
            current_node = queue.popleft()
            level_nodes.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.appendleft(level_nodes)

    return result

def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)

    print(str(traverse(root)))

main()