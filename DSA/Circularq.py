class CircularQueue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.front = -1
        self.rear = -1
        self.queue = [None] * max_size

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            return "[]"
        if self.front <= self.rear:
            return str(self.queue[self.front:self.rear + 1])
        else:
            return str(self.queue[self.front:] + self.queue[:self.rear + 1])

def main():
    max_size = int(input("Enter the size of the queue: "))
    q = CircularQueue(max_size)
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
