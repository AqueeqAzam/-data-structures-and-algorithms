class Node:
  def __init__(self, data) -> None:
    self.left = None
    self.right = None
    self.data = data

  def show(self):
    if self.left:
      self.left.show()
    print(self.data)
    if self.right:
      self.right.show()


root = Node(100)
root_left = Node(99)
root_right = Node(101)
root.left = root_left
root.right = root_right
root.show()

#-------------Tree Traverse----------------
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def preorder(root):
    if root:
        # Traverse root
        print(str(root.val) + '->', end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)
def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + '->', end='')
        # str covert value in string datatype
        # Traverse right
        inorder(root.right)


def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Treaverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + '->', end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(43)
root.left.left.left = Node(41)

print('Preorder traverse')
preorder(root)


print('Inorder traverse')
inorder(root)

print('Postrder traverse')
postorder(root)
