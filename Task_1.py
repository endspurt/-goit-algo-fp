class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list.sorted_insert(Node(current.data))
            current = next_node
        self.head = sorted_list.head

    def merge_sorted_lists(self, llist1, llist2):
        dummy = Node(0)
        tail = dummy
        while llist1 is not None and llist2 is not None:
            if llist1.data <= llist2.data:
                tail.next = llist1
                llist1 = llist1.next
            else:
                tail.next = llist2
                llist2 = llist2.next
            tail = tail.next
        if llist1 is not None:
            tail.next = llist1
        else:
            tail.next = llist2
        return dummy.next

# Приклад використання
llist = LinkedList()
llist.head = Node(3)
llist.head.next = Node(1)
llist.head.next.next = Node(2)

print("Оригінальний список:")
current = llist.head
while current:
    print(current.data, end=" ")
    current = current.next

llist.reverse()
print("\nПеревернутий список:")
current = llist.head
while current:
    print(current.data, end=" ")
    current = current.next

llist.insertion_sort()
print("\nВідсортований список:")
current = llist.head
while current:
    print(current.data, end=" ")
    current = current.next

llist1 = LinkedList()
llist1.head = Node(1)
llist1.head.next = Node(3)
llist1.head.next.next = Node(5)

llist2 = LinkedList()
llist2.head = Node(2)
llist2.head.next = Node(4)
llist2.head.next.next = Node(6)

merged_list_head = llist.merge_sorted_lists(llist1.head, llist2.head)
print("\nОб'єднаний відсортований список:")
current = merged_list_head
while current:
    print(current.data, end=" ")
    current = current.next
