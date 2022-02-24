class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def middle_of_linked_list(head):
    slow, fast = head, head

    while True:
        slow = slow.next
        fast = fast.next.next

        if fast is None or fast.next is None:
            return slow.value

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    print(middle_of_linked_list(head))

main()