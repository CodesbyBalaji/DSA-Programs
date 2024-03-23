class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.front = -1
        self.rear = -1
        self.queue = []

    def is_full(self):
        return self.rear == self.max_size - 1

    def is_empty(self):
        return self.front == -1 or self.rear == -1

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = self.rear + 1
        self.queue.append(item)
        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.front = self.front + 1
        item = self.queue.pop(0)
        if self.front == self.max_size:
            self.front = 0
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def __str__(self):
        return str(self.queue)


def main():
    max_size = int(input("Enter the size of the queue: "))
    q = Queue(max_size)
    while True:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item to enqueue: ")
            try:
                q.enqueue(item)
            except Exception as e:
                print(e)
        elif choice == 2:
            try:
                print(q.dequeue())
            except Exception as e:
                print(e)
        elif choice == 3:
            try:
                print(q.peek())
            except Exception as e:
                print(e)
        elif choice == 4:
            print(q)
        elif choice == 5:
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()