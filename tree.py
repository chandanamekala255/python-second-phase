class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        
class Tree:
    def inorder(root):
        if root!=None:
            Tree.inorder(root.left)
            print(root.data,end=" ")
            Tree.inorder(root.right)
    def preorder(root):
        if root!=None:
            print(root.data,end=" ")
            Tree.preorder(root.left)
            Tree.preorder(root.right)
    def postorder(root):
        if root!=None:
            Tree.postorder(root.left)
            Tree.postorder(root.right)
            print(root.data,end=" ")
#these are the values in tree
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
#these line for only print data in tree
print(root.left.left.data)

#these sre used to print the dfs

Tree.inorder(root)
print()
Tree.preorder(root)
print()
Tree.postorder(root)






#output
40
inorder:40 20 10 50 30 
preorder:10 20 40 30 50 
postorder40 20 50 30 10 

