# Given the head of a Singly LinkedList, write a function to determine if the 
# LinkedList has a cycle in it or not.

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def has_cycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print(has_cycle(head))

  head.next.next.next.next.next.next = head.next.next
  print(has_cycle(head))

main()