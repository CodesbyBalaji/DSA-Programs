# queue using linklist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        n = Node(data, None)

        if self.front is None:
            self.front = n
            self.rear = n

        else:
            self.rear.next = n
            self.rear = n

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return

        t = self.front
        print("Deqeue:", t.data)
        self.front = self.front.next
        t = None

        if self.front is None:
            self.rear = None

    def display(self):
        n = self.front

        while n:
            print(n.data)
            n = n.next

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
            return
        else:
            print(self.front.data)


INode = Linklist()
while (1):
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Peek")
    print("5.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        node = int(input("Enter the data:"))
        INode.enqueue(node)
    elif choice == 2:
        INode.dequeue()
    elif choice == 3:
        INode.display()
    elif choice == 4:
        INode.peek()
    else:
        break