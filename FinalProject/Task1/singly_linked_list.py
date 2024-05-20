
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
 
class LinkedList:
    
    def __init__(self):
        self.head = None
 
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
 
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
  
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node
 
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
  
    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next
 
    def remove_last_node(self):
 
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None
 
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
 
    def remove_node(self, data):
        current_node = self.head
 
        if current_node.data == data:
            self.remove_first_node()
            return
 
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
 
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0
 
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    
    # Function to reverse the linked list
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    # Function to sort the linked list using insertion sort
    def insertionSort(self):
        sorted_head = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            sorted_head = self.sortedInsert(sorted_head, current_node)
            current_node = next_node

        self.head = sorted_head

    def sortedInsert(self, head, node):
        if head is None or head.data >= node.data:
            node.next = head
            head = node
        else:
            current = head
            while current.next is not None and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return head
    
    # Function to merge two sorted linked lists
    def mergeTwoLists(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 is not None and l2 is not None:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1 is not None:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next
