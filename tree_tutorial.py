class Node: #This will define the Nodes and how they work within the Tree
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None
        
def inorder_traversal(root): #This function will demonstrate In Order Traversal
    if root:
        inorder_traversal(root.left)
        print(str(root.item) + "->", end='')
        inorder_traversal(root.right)
    
def postorder_traversal(root): #This function will demonstrate Post-Order Traversal
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(str(root.item) + "->", end='')


def preorder_traversal(root): #This function will demonstrate Pre-Order Traversal
    if root:
        print(str(root.item) + "->", end='')
        preorder_traversal(root.left)
        preorder_traversal(root.right)
    
root = Node(1) #These will establish the variables within each node
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In order traversal: ")

inorder_traversal(root)

print("\nPre-order traversal: ")
preorder_traversal(root)

print("\nPost-order traversal: ")
postorder_traversal(root)

"""
Output:

In order traversal:
4->2->5->1->3->
Pre-order traversal:
1->2->4->5->3->
Post-order traversal:
4->5->2->3->1->
"""

