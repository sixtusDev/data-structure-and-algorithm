# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to the first node of the next level.

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None, next=None)-> None:
        self.value = value
        self.left = left
        self.right = right
        self.next = next

    def print_all_level_order(self):
        current = self

        while current:
            print(str(current.value) + " ", end="")
            current = current.next


def connect_all_level_order(root):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        level_length = len(queue)

        for _ in range(level_length):
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            if queue:
                current_node.next = queue[0]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    connect_all_level_order(root)

    root.print_all_level_order()

main()