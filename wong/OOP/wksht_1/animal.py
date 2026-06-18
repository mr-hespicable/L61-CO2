class Animal:
    def __init__(self, s: str, n: int):
        self.__state: str = s
        self.__size: int = n

    def feed(self) -> None:
        self.__size += 1
        if self.__size == 5:
            self.__state = "FISH"

    def getState(self) -> str:
        return self.__state

    def getSize(self) -> int:
        return self.__size



thisFish = Animal("Fish", 1)

print(thisFish.getState(), end="")
print(" is of size", thisFish.getSize())

while thisFish.getState() != "FISH":
    thisFish.feed()

print("It is now a big ", end="")
print(thisFish.getState())

