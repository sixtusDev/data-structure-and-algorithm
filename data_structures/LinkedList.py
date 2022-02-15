class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_the_beginning(self, value) -> None:
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def insert_values(self, values) -> None:
        self.head = None
        for value in values:
            self.insert_at_end(value)

    def get_length(self) -> int:
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def remove_at(self, index) -> None:
        if index < 0 or index > self.get_length() - 1:
            raise Exception("Index out of bound")

        if index == 0:
            self.head = self.head.next
            return

        node = self.head
        count = 0
        while node:
            if count == index - 1:
                node.next = node.next.next
                break
            count += 1
            node = node.next

    def insert_at(self, index, value) -> None:
        if index < 0 or index > self.get_length() - 1:
            raise Exception("Index out of bound")
        
        node = self.head
        count = 0
        while node:
            if count == index:
                node.next = Node(node.data, node.next)
                node.data = value
                break
            count += 1
            node =  node.next
            

    def print(self) -> None:
        node = self.head
        if node is None:
            return "Linked list is empty"
        list_str = ""

        while node:
            list_str += f"{str(node.data)}->"
            node = node.next
        print(list_str)


linked_list = LinkedList()
linked_list.insert_at_the_beginning(10)
linked_list.insert_at_the_beginning(20)
linked_list.insert_at_the_beginning(30)
linked_list.insert_at_the_beginning(40)
linked_list.insert_at_end(5)
linked_list.insert_values([1,2,3,4,5,6,7,8,9])
linked_list.remove_at(0)
linked_list.insert_at(2, 10)
print(linked_list.get_length())
linked_list.print()
