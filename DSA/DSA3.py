class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
            return None

        data = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None

        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Queue:", end=" ")
        n = self.front
        while True:
            print(self.queue[n], end=" ")
            if n == self.rear:
                break
            n = (n + 1) % self.capacity
        print()
def main():
    capacity = int(input("Enter the capacity of the Queue: "))
    queue = Queue(capacity)

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the value to enqueue: "))
            queue.enqueue(item)
        elif choice == 2:
            item = queue.dequeue()
            if item is not None:
                print("Dequeued item:", item)
        elif choice == 3:
            item = queue.peek()
            if item is not None:
                print("Front of the queue:", item)
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()
