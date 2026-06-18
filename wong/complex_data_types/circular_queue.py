# NOTE: this code uses global variables where necessary as a conceptual exercise
# Tutorial 3 demonstrates better implementations using classes

class Queue:
    def __init__(self, size: int):
        self.__size = size
        self.__queue = [0] * self.__size
        self.__head = 0
        self.__tail = -1
        self.__count = 0

    def __repr__(self):
        return f"{*self.__queue,}"

    def is_empty(self):
        return self.__count == 0


    def is_full(self):
        return self.__count == self.__size


    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue full error")
        self.__tail += 1
        self.__head = (self.__head + 1) % self.__size
        self.__queue[self.__tail % self.__size] = item

        self.__count += 1


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue empty error")

        t = self.__queue[self.__head % self.__size]
        self.__head = (self.__head + 1) % self.__size

        self.__count -= 1
        return t




###############
# MAIN PROGRAM
###############

q = Queue(10)

for i in range(1, 11):
    q.enqueue(i)

print("Full check:", q.is_full())
print("queue:", q)


while not q.is_empty():
    print(q.dequeue())

print("Empty check:", q.is_empty())

q.enqueue(10)

for i in range(1, 10):
    q.enqueue(i)
    print(q, i)

print("Full check:", q.is_full())


while not q.is_empty():
    print(q.dequeue())

print("Empty check:", q.is_empty())
