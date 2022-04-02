# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to the first node of the next level.

# from inspect import stack
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def has_path(root, target_sum):
    if root is None:
        return
    
    stack_ = deque()
    stack_.append(root)

    sum = 0

    while stack_:
        current_node = stack_.pop()
        sum += current_node.value
        print(sum)
        if sum == target_sum and not current_node.right and not current_node.left:
            return True

        if current_node.left:
            stack_.append(current_node.left)
        if current_node.right:
            stack_.append(current_node.right)

        if not current_node.right and not current_node.left:
            sum -= current_node.value

    return False
    
    


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(has_path(root, 28))

main()