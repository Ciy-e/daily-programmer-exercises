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