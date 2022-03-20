from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        current_size = len(queue)
        current_level = []

        for _ in range(current_size):
            current_node = queue.popleft()

            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)

    return result


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)

    print(str(traverse(root)))

main()




