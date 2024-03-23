class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Unable to enqueue item:", item)
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print("Enqueued item:", item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue.")
            return None

        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print("Dequeued item:", item)
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Current Queue:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

if __name__ == "__main__":
    size = int(input("Enter the size of the circular queue: "))
    queue = CircularQueue(size)

    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
