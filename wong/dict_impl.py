# dictionary implement

class defaultlist(list):
    def __init__(self):
        pass
    def __setitem__(self, index, value):
        while len(self) <= index:
            self.append(None)
        list.__setitem__(self, index, value)

def hashh(k) -> int:
    return int(str(abs(hash(str(k))))[:10])

class Dictionary:
    def __init__(self):
        # hash, data
        self.k = defaultlist()
        self.v = defaultlist()

    def clear(self):
        self.v = defaultlist()

    def __getitem__(self, k):
        return self.v[hashh(k)]

    def __setitem__(self, key, value):
        self.k[hashh(key)] = key
        self.v[hashh(key)] = value
        self.v[hashh(key)] = value

    def __repr__(self):
        return str((self.k, self.v))
            
    def remove(self, key):
        self.k[hashh(key)] = None
        self.v[hashh(key)] = None

    def keys(self):
        

    def values(self):
        return self.v

    def __len__(self):
        return len(self.k)



# 1. Initialization
my_dict = Dictionary()
print("--- Testing Dictionary Class ---")

# 2. Testing add() and write()
my_dict["CPU"] = "Central Processing Unit"
my_dict["RAM"] = "Random Access Memory"
my_dict["ALU"] = "Arithmetic Logic Unit"

# Expected Output: Added 3 items. Current length: 3
print(f"Added 3 items. Current length: {len(my_dict)}")

# 3. Testing keys() and values()
# Expected Output: Keys: ['CPU', 'RAM', 'ALU']
print(f"Keys: {my_dict.keys()}")

# Expected Output: Values: ['Central Processing Unit', 'Random Access Memory', 'Arithmetic Logic Unit']
print(f"Values: {my_dict.values()}")

# 4. Testing Update (writing to an existing key)
my_dict["RAM"] = "Volatile Memory"

# Expected Output: Updated RAM value: Volatile Memory
print(f"Updated RAM value: {my_dict.values()[1]}")

# 5. Testing remove()
print("\nRemoving 'ALU'...")
my_dict.remove("ALU")

# Expected Output: New length: 2
print(f"New length: {len(my_dict)}")

# Expected Output: Remaining keys: ['CPU', 'RAM']
print(f"Remaining keys: {my_dict.keys()}")

# 6. Testing clear()
print("\nClearing dictionary...")
my_dict.clear()

# Expected Output: Final length: 0
print(f"Final length: {len(my_dict)}")

# Expected Output: Final keys list: []
print(f"Final keys list: {my_dict.keys()}")
