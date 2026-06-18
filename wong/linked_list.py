class StaticArrayLinkedList:
    def __init__(self, size=10):
        """
        Initialize the linked list with a fixed size.
        """
        self.max_size = size

        # 1. The Data Array (stores values)
        self.data = [None] * size

        # 2. The Pointer Array (stores index of next node)
        self.next_index = [None] * size

        # 3. Pointers
        self.head = -1  # -1 represents NULL (end of list)
        self.free = 0  # Points to the first available slot

        # Initialize the 'free list'
        # Each slot points to the next one, creating a chain of empty slots.
        for i in range(size - 1):
            self.next_index[i] = i + 1
        self.next_index[size - 1] = -1  # Last free slot points to NULL

    def find(self, item) -> bool:
        return self.pos(item) != -1

    def pos(self, item) -> int:
        i = 0
        c = self.head
        found = False

        while found is False and i <= self.max_size:
            if self.data[c] == item:
                found = True
                return i+1
            else:
                i += 1
                c = self.next_index[c]
        return -1

    def is_full(self):
        return self.free == -1

    def is_empty(self):
        return self.head == -1

    def insert_at_start(self, value):
        """
        Inserts a new value at the beginning of the list.
        """
        if self.is_full():
            print(f"Error: List is full. Cannot insert '{value}'.")
            return

        # 1. Get a free slot
        new_node_index = self.free
        self.free = self.next_index[self.free]  # Move free pointer to next available

        # 2. Add data
        self.data[new_node_index] = value

        # 3. Adjust pointers
        self.next_index[new_node_index] = self.head  # New node points to old head
        self.head = new_node_index  # Head now points to new node

        print(f"Inserted '{value}' at index {new_node_index}")

    def insert_after(self, target_val, new_val):
        """
        Finds a node with target_val and inserts new_val after it.
        """
        if self.is_full():
            print("Error: List is full.")
            return

        current = self.head
        found = False

        # Traverse to find the target
        while current != -1:
            if self.data[current] == target_val:
                found = True
                break
            current = self.next_index[current]

        if not found:
            print(f"Error: Value '{target_val}' not found.")
            return

        # 1. Get a free slot
        new_node_index = self.free
        self.free = self.next_index[self.free]

        # 2. Add data
        self.data[new_node_index] = new_val

        # 3. Adjust pointers
        self.next_index[new_node_index] = self.next_index[current]
        self.next_index[current] = new_node_index

        print(f"Inserted '{new_val}' after '{target_val}' at index {new_node_index}")

    def delete(self, value):
        """
        Removes the first occurrence of value from the list.
        """
        if self.is_empty():
            print("Error: List is empty.")
            return

        current = self.head
        previous = -1

        # Search for the node
        while current != -1 and self.data[current] != value:
            previous = current
            current = self.next_index[current]

        # Value not found
        if current == -1:
            print(f"Error: Value '{value}' not found.")
            return

        # Case 1: Deleting the head node
        if current == self.head:
            self.head = self.next_index[current]
        # Case 2: Deleting a middle or end node
        else:
            self.next_index[previous] = self.next_index[current]

        # Add the deleted node back to the free list
        self.data[current] = None  # Optional: Clear data for clarity
        self.next_index[current] = self.free
        self.free = current

        print(f"Deleted '{value}' from index {current}")

    def traverse(self):
        """
        Prints the logical order of the linked list.
        """
        if self.is_empty():
            print("List is empty.")
            return

        print("\n--- Current Linked List ---")
        current = self.head
        while current != -1:
            print(
                f"Index [{current}]: Data = {self.data[current]} -> Next Index = {self.next_index[current]}"
            )
            current = self.next_index[current]
        print("---------------------------\n")

    def debug_view(self):
        """
        Helper to show the raw arrays for students to see the internal state.
        """
        print("\n[DEBUG] Internal Memory State:")
        print(f"HEAD: {self.head}, FREE: {self.free}")
        print(f"Index\tData\tNext")
        for i in range(self.max_size):
            print(f"{i}\t{self.data[i]}\t{self.next_index[i]}")
        print()


# --- Main Program Showcase ---

if __name__ == "__main__":
    # 1. Create a list of size 5
    my_list = StaticArrayLinkedList(size=5)

    # 2. Insert items
    my_list.insert_at_start("Apple")
    my_list.insert_at_start("Banana")
    my_list.insert_at_start("Cherry")

    my_list.traverse()
    my_list.debug_view()

    # 3. Insert in the middle
    my_list.insert_after("Banana", "Date")  # Should go after Banana

    my_list.traverse()

    # 4. Delete an item
    my_list.delete("Banana")

    my_list.traverse()
    my_list.debug_view()

    # 5. Fill the list to trigger overflow error
    my_list.insert_at_start("Elderberry")
    my_list.insert_at_start("Fig")
    my_list.insert_at_start("Grape")  # This should fail as size is 5

    print(my_list.find("Grape"))
    print(my_list.pos("Elderberry"))
