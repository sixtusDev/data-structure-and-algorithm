# Find the minimum depth of a binary tree. The minimum depth is the number of nodes 
# along the shortest path from the root node to the nearest leaf node.

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimum_depth(root):
    result = 1
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_length = len(queue)

        for _ in range(level_length):
            current_node = queue.popleft()

            if not current_node.left and not current_node.right:
                return result
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result = result + 1

    return result

            


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Minimum depth: ", minimum_depth(root))

main()