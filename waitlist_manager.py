# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
            return f"{name} was added to the waitlist."
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"{name} was added to the waitlist."
    
    def remove(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev is None:
                    # Node to remove is the head
                    self.head = current.next
                else:
                    prev.next = current.next
                return f"{name} was removed from the waitlist."
            prev = current
            current = current.next
        return f"{name} not found"
    
    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return
        current = self.head
        while current:
            print(current.name)
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            print(f"{name} was added to the front of the waitlist.")

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            message = waitlist.add_end(name)
            print(message)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            message = waitlist.remove(name)
            print(message)
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work? It works as a linked list, where each customer is held as a node on the list. 
- What role does the head play? It is a reference to the first node on the list. It's used as the entry point for the list, such as for adding or removing nodes. Without the head, you can't access the nodes.
- When might a real engineer need a custom list like this? This would mainly be used with data that constantly changes or inserts/deletes, like queues or waitlists. It would also be useful when the size of the data set is unknown.
'''
