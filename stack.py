class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.item = []

    # Push an item onto the stack
    def push(self, item):
        self.item.append(item)
    
     # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if len(self.item) == 0:
            return "Stack is empty"
        else:
            return self.item.pop()
    
    def peek(self):
        if len(self.item) == 0:
            return "Stack is empty"
        else:
            return self.item[len(self.item) - 1]
        
     # Check if the stack is empty
    def is_empty(self):
        return len(self.item) == 0
    
     # Display the items in the stack
    def display(self):
        print("Stack items:", self.item)
    


if __name__ == '__main__':
    s = Stack()
    print(s)
    s.push(1)
    s.push(4)
    s.display()

    print("Popped item:", s.pop())

    # Display the updated items in the stack
    s.display()
  


