class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def find_cycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return fast
    return None

def find_cycle_start(head):
    fast = find_cycle(head)

    if fast is not None:
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return slow.value
    return False

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next

    print(find_cycle_start(head))

main()
