from unittest import result


class Node:
    def __init__(self, value, next=None):
        self.value = value,
        self.next = next

    def print_list(self):
        temp = self

        while temp is not None:
            print(temp.value, end="=>")
            temp = temp.next
        print()

def reverse_linked_list(head):
    current, previous, next = head, None, None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    reversed_list = reverse_linked_list(head)
    reversed_list.print_list()

main()