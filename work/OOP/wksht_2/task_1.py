from typing import override

class Animal:
    def __init__(self, s: str, n: int):
        self._state: str = s
        self._size: int = n

    def feed(self) -> None:
        self._size += 1
        print(f"{self._state} fed")

    def getState(self) -> str:
        return self._state

    def getSize(self) -> int:
        return self._size


class Fish(Animal):
    def __init__(self, s: int):
        super().__init__(s, 1)
        self.__maxSize: int = 2

    def setMaxSize(self, m: int):
        self.__maxSize = m

    @override
    def feed(self):
        self._size += 2
        print(f"{self._state} fed")
        if self._size >= self.__maxSize:
            self._state = "BIG FISH"

class Duck(Animal):
    def __init__(self, s: str, n: int):
        super().__init__(s, n)

    @override
    def feed(self):
        super().feed()
        if self._size == 5:
            self._state = "BIG DUCK"



thisFish = Fish("little fish")
thisFish.setMaxSize(3)

thisDuck = Duck("little duck", 1)

for count in range(1, 4):
    thisDuck.feed()
    print(thisDuck.getState())
    thisFish.feed()
    print(thisFish.getState())
