Introduction:

A Tree represents a collection of nodes that are connected in such a way that resembles a tree structure. There is one root node that has a number of child nodes, and each child node has additional child nodes of their own, and so on and so forth. Each node must be connected to exactly one parent node, with the one exception being the root node.

Uses, and why Tree is a useful Data Structure:

Each node within a tree is capable of holding one or more sets of data, such as variables and functions. Due to the way Trees are structured, looping through each node down one descending line is not as practical as it initially sounds. This can, however, be accomplished through recursion, or the practice by which a function can call upon itself multiple times. If done correctly, a recursive function can pull data from the nodes within a Tree as many times as it needs to in order to accomplish its ultimate purpose. There are different means of recursively traversing through the Nodes of a tree. In Order Traversal will go through all the nodes in the subtree on the left, then the root node, and finally all the nodes in the subtree on the right. Pre-Order Traversal begins by going through the root node, and then all the nodes in each subtree, first on the left, and then on the right. Lastly, Post-Order Traversal will first go through all the nodes in the subtree on the left, then all the nodes on the right subtree, and finally ending at the root node.Trees can be especially useful for displaying such things as family trees, either with an ascending list of ancestors, or a descending list of descendants.

Big O notation:

If the search is done with a linked list of dynamic array, O(n)

If the search is done on a Binary Search Tree with esclusion of sub-branches, O(log n)

Example problem:
```python
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
root.right = Node(4)
root.left.left = Node(8)
root.left.right = Node(16)

print("In order traversal: ")

inorder_traversal(root)

print("\nPre-order traversal: ")
preorder_traversal(root)

print("\nPost-order traversal: ")
postorder_traversal(root)

"""
Output:

In order traversal:
8->2->16->1->4->
Pre-order traversal:
1->2->8->16->4->
Post-order traversal:
8->16->2->4->1->
"""
```

The following links lead to a practice problem. In this example, you are tasked with creating your own binary tree from scratch. The nodes must consist of a root node with the value 2 stored in it, two children nodes of that root node with values of 3 and 4 respectively, and then the children nodes of those must include the numbers that result from the root being both added to, and multiplied by their corrresponding parent nodes (one node must contain the answer to the addition, the other must contain the answer to the multiplication). Then you must traverse through your tree using each of the three recursive traversal methods demonstrated in the example problem.

On Github:
[Tree Practice](https://github.com/JoshuaCapron64/cse212-final-project/blob/main/tree_tutorial.py)

On VSCode:
[Tree Practice](tree_tutorial.py)

Back to Welcome:

On Github:
[Welcome](https://github.com/JoshuaCapron64/cse212-final-project/blob/main/welcome.md)

On VSCode:
[Welcome](welcome.md)