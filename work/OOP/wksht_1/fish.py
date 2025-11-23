class Fish:
    def __init__(self, state: str, size: int):
        self.state: str = state
        self.size: int = size

    def feed(self):
        self.size += 1
        print("fish fed meow")
        if self.size == 5:
            self.state = "FISH"


ts_fish = Fish("fih...", 1)

print(f"{ts_fish.state} is of size {ts_fish.size}")

while ts_fish.state != "FISH":
    ts_fish.feed()

print(f"it is now a chungus {ts_fish.state}!!!!!!!!!!!!")
