# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

# recursive implementation of tree height in python
def height(root):
        if root:
            return 1 + max(height(root.left), height(root.right))
        else:
            return -1

#checks if a tree is a Binary Search Tree
def checkBST(root):
    stack = []
    data_list = []
    def inorder(root):
        if root:
            inorder(root.left)
            data_list.append(root.data)
            inorder(root.right)
        
    inorder(root)

    # is every element distinct?
    if len(data_list) > len(set(data_list)):
        return False
    return data_list == sorted(data_list)