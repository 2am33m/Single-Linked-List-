class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append_at_begining(self,data):
        """Append the data at the begining of the linked list."""
        node = Node(data, self.head)
        node.next = self.head
        self.head = node

    def print_LL(self):
        """Print the entire linked list"""
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head

        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next
        print(itr)

    def append_at_end(self,data):
        """Append data at the end of the linked list."""
        node = Node(data)

        if self.head is None: 
            self.head = node    
            return

        current = self.head
        while current.next:
            current = current.next 
        current.next = node

    def append_anywhere(self, previous_node_data, data,):
        """Append node after the previous node"""
        current = self.head 
        while current.next is not None and current.data != previous_node_data:
            current = current.next

        if current.data != previous_node_data:
            print("Previous node data is not found")
            return
        node = Node(data)
        node.next = current.next
        current.next = node




llist = LinkedList()
        
llist.append_at_end(10)
llist.append_at_end(20)
llist.append_at_end(30)

llist.print_LL()


# Append at the begining 
llist.append_at_begining(0)

llist.print_LL()

# Append after a previous node 

llist.append_anywhere(20,25)

llist.print_LL()


