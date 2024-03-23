class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, key):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if current == self.head:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return
        prev = None
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                return
        print(f"Element {key} not found in the list.")

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

# Creating a Circular Linked List
circular_linked_list = CircularLinkedList()

while True:
    print("\nCircular Linked List Operations:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete Element")
    print("5. Display")
    print("6. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element to insert at beginning: "))
        circular_linked_list.insert_beginning(data)
    elif choice == 2:
        data = int(input("Enter element to insert at end: "))
        circular_linked_list.append(data)
    elif choice == 3:
        data = int(input("Enter element to insert: "))
        position = int(input("Enter position: "))
        circular_linked_list.insert_at_position(data, position)
    elif choice == 4:
        key = int(input("Enter element to delete: "))
        circular_linked_list.delete(key)
    elif choice == 5:
        circular_linked_list.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

