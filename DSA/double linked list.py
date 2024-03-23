class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Doubly_Link_list:
    def __init__(self):
        self.head = None

    def display_frw(self):
        if self.head is None:
            print("The link_list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} ---> ", end="")
                n = n.nref

    def insert_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n


    def delete_begin(self):
        if self.head is None:
            print("Doubly_Link_list is empty, can't deleat!!")
            return
        if self.head.nref is None:
            self.head = None
            print("Doubly_Link_list is empty after deleating a Node!!")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("Doubly_Link_list is empty, can't deleat!!")
            return
        if self.head.nref is None:
            self.head = None
            print("Doubly_Link_list is empty after deleating a Node!!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None


dll = Doubly_Link_list()
while True:
    print('''
    1. Add_data front:
    2. Add_data end:
    3. Delete_data in front:
    4. Delete_data in end:
    5. Display the Linkedlist:
    6. Exit
''')
    cho = int(input("Enter your choice:"))
    if cho == 1:
        n = int(input("Enter a data:"))
        dll.insert_begining(n)
    elif cho == 2:
        n = int(input("Enter a data:"))
        dll.insert_end(n)
    elif cho == 3:
        dll.delete_begin()
    elif cho == 4:
        dll.delete_end()
    elif cho == 5:
        dll.display_frw()
    elif cho == 6:
        break
    else:
        print("Invalid Input :(")
