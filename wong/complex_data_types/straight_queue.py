# NOTE: this code uses global variables where necessary as a conceptual exercise
# Tutorial 3 demonstrates better implementations using classes

class Queue:
    def __init__(self, size: int):
        self.__size = size
        self.__queue = [0] * self.__size
        self.__head = 0
        self.__tail = -1

    def __repr__(self):
        return f"{self.__queue,} {self.__head}, {self.__tail}"

    def is_empty(self):
        return self.__head > self.__tail


    def is_full(self):
        return self.__tail == self.__size - 1


    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue full error")
        self.__tail += 1
        self.__queue[self.__tail] = item


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue empty error")
        t = self.__queue[self.__head]
        self.__head += 1
        return t




###############
# MAIN PROGRAM
###############

q = Queue(10)

for i in range(1, 10):
    q.enqueue(i)

print("Full check:", q.is_full())


while not q.is_empty():
    print(q.dequeue())

print("Empty check:", q.is_empty())

q.enqueue(9)

# can you see why this will raise an exception even though the queue only
# contains one element?
try:
    q.enqueue(10)
except Exception as err:
    print("error:", err)
