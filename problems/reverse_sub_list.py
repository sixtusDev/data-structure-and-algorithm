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

def reverse_sub_list(head, p, q):
    if p == q:
        return head

    current, previous = head, None
    i = 1
    while i < p:
        previous = current
        current = current.next
        i = i + 1
    
    first_last_node = previous

    i = 1
    while i < q:
        next = current.next
        current.next = previous
        previous = current
        current = current.next
    
    
    


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # reversed_list = reverse_linked_list(head)
    # reversed_list.print_list()

main()