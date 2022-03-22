# Given a binary tree and a node, find the level order successor of the given node in the tree. 
# The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val,
        self.left = left
        self.right = right

def find_successor(root, key):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.val == key:
                if queue and queue[0]:
                    return queue[0].val
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return None

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    succesor = find_successor(root, 12)
    print(succesor)

main()