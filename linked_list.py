class LinkedList:
  def __init__(self):
    self.head = None

    # insertion method
  def insert(self, data):
   newNode = Node(data)
   if self.head is None:
        self.head = newNode
        return
   else:
        newNode.next = self.head
        self.head = newNode

    # traversing method
  def traverse(self):
      current = self.head
      while (current):
        print(current.data)
        current = current.next


  def delete(self):
    if self.head == None:
      return
    self.head = self.head.next

  def size(self):
    size = 0
    if self.head:
      current = self.head
      while(current):
        size = size + 1
        current = current.next
        return size
    else:
      return 0






L = LinkedList()
print('Inserted in liked list are:')
L.insert('56')
L.insert(82)
L.insert(76)
L.insert(89)
L.traverse()
print('Dleted elements is:')
L.delete()
L.traverse()
print('list size is:')
L.size()
