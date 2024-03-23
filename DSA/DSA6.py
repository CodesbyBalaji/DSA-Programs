# stack using linklist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None

    def push(self, data):
        n = Node(data, self.head)
        self.head = n

    def pop(self):
        if self.head is None:
            print("stack is empty")
            return
        t = self.head
        self.head = self.head.next
        print("Poped items:", t.data)
        t = None

    def display(self):
        if self.head is None:
            print("stack is empty")
            return
        n = self.head
        while n:
            print(n.data)
            n = n.next

    def peek(self):
        if self.head is None:
            print("stack is empty")
        else:
            print(self.head.data)

csc = Linklist()
while (1):
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Peek")
    print("5.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        n = int(input("Enter a data:"))
        csc.push(n)
    elif choice == 2:
        csc.pop()
    elif choice == 3:
        csc.display()
    elif choice == 4:
        csc.peek()
    else:
        break

