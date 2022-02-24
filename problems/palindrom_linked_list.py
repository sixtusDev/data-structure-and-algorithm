class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

## Finds the middle element of the linked list
def middle_linked_list(head):
    slow, fast = head, head

    while True:
        slow = slow.next
        fast = fast.next.next

        if fast is None or fast.next is None:
            return slow

def is_palindrome_linked_list(head):
    middle = middle_linked_list(head)
    
    ## Reverse the linked list
    prev = None
    while middle:
        temp = middle.next
        middle.next = prev
        prev = middle
        middle = temp

    ## Check for palindrome
    left_pointer, right_pointer = head, prev
    while right_pointer:
        if left_pointer.value != right_pointer.value:
            return False
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    return True


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    # head.next.next.next.next.next = Node(0)

    print(is_palindrome_linked_list(head))

main()
