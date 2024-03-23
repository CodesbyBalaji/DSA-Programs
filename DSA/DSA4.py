class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range.")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def insert_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n

    def delete(self, key):
        if self.head is None:
            print("Linked List is empty.")
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        prev = None
        temp = self.head
        while temp is not None:
            if temp.data == key:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
        print(f"Element {key} not found in the list.")

    def display(self):
        n = self.head
        while n: 
            print(n.data, end=" -> ")
            n=n.next
        print("None")

# Creating a Linked List
linked_list = LinkedList()

while True:
    print("\nLinked List Operations:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete Element")
    print("5. Display")
    print("6. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element to insert at beginning: "))
        linked_list.insert_beginning(data)
    elif choice == 2:
        data = int(input("Enter element to insert at end: "))
        linked_list.insert_end(data)
    elif choice == 3:
        data = int(input("Enter element to insert: "))
        position = int(input("Enter position: "))
        linked_list.insert_at_position(data, position)
    elif choice == 4:
        key = int(input("Enter element to delete: "))
        linked_list.delete(key)
    elif choice == 5:
        linked_list.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
