# Given a binary tree, populate an array to represent its zigzag level order traversal. 
# You should populate the values of all nodes of the first level from left to right, 
# then right to left for the next level and keep alternating in the same manner for the following levels

from collections import deque
import queue
from unittest import result


class TreeNode:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    left_to_right = True

    while queue:
        level_nodes = deque()
        level_length = len(queue)

        for _ in range(level_length):
            current_node = queue.popleft()
            if left_to_right:
                level_nodes.append(current_node.value)
            else:
                level_nodes.appendleft(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(level_nodes)

        left_to_right = not left_to_right

    return result



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)

    print(str(traverse(root)))

main()