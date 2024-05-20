
from singly_linked_list import *

# Create a linked list and add some nodes
ll = LinkedList()
ll.insertAtEnd(3)
ll.insertAtEnd(1)
ll.insertAtEnd(2)

# Reverse the linked list
ll.reverse()
ll.printLL()  # Output should be the reversed list

# Sort the linked list
ll.insertionSort()
ll.printLL()  # Output should be the sorted list

# Merge two sorted linked lists
ll1 = LinkedList()
ll1.insertAtEnd(1)
ll1.insertAtEnd(3)
ll1.insertAtEnd(5)

ll2 = LinkedList()
ll2.insertAtEnd(2)
ll2.insertAtEnd(4)
ll2.insertAtEnd(6)

merged_ll = LinkedList()
merged_ll.head = merged_ll.mergeTwoLists(ll1.head, ll2.head)
merged_ll.printLL()  # Output should be the merged sorted list