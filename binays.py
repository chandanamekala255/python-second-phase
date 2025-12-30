class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, element):
    if root==None:
        return False

    if root.data == element:
        return True
    elif element < root.data:
        return search(root.left, element)
    else:
        return search(root.right, element)

root = Node(100)
root.left = Node(20)
root.right = Node(110)
root.left.left = Node(5)
root.left.right = Node(25)
root.right.left = Node(105)
root.right.right = Node(120)

print(search(root, 120))  
print(search(root, 90))  




#output
#true
#false
