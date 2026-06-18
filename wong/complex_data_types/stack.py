class Stack:
    def __init__(self, size):
        self.__size = size
        self.__stack = [None] * self.__size
        # [None, None, None, None, None] when size == 5
        self.__top = -1

    def push(self, data):
        if not self.is_full():
            self.__stack[self.__top] = data
            self.__top += 1

        else:
            err = "Cannot push to a full stack"
            raise OverflowError(err)

    def pop(self):
        if not self.is_empty():
            t = self.__stack[self.__top]
            self.__top -= 1
            return t
        
        else:
            err = "Cannot pop an empty stack"
            raise IndexError(err)

    def peek(self):
        if not self.is_empty():
            return self.__stack[self.__top-1]

        else:
            err = "Stack is empty"
            raise IndexError(err)

    def is_full(self):
        return self.__top == self.__size-1

    def is_empty(self):
        return self.__top == -1


s = Stack(5) # stack of size 5

s.push(6)
s.push(7)

print(s.pop())
print(s.peek())
s.push(8)
print(s.pop())
#[6, None, None, None, None]
s.push(9)
s.push(10)
s.push(11)
s.push(12)
print(s.peek())
print(s.is_full())

try:
    s.push(13)
except Exception as e:
    print("error: ", end="")
    print(e)


print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.is_empty())

try:
    print(s.pop())
except Exception as e:
    print("error: ", end="")
    print(e)

try:
    print(s.peek())
except Exception as e:
    print("error: ", end="")
    print(e)

s.push(4)
print(s.peek())
