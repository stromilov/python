#         7
#       /   \
#      4     8
#    /   \  
#   2     6
                  
                  
from turtle import right


class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
    
tree =            TreeNode(7)
tree.left =       TreeNode(4)
tree.right =      TreeNode(8)
tree.left.left =  TreeNode(2)
tree.left.right = TreeNode(6)


def pre_order(node):
    if node.left.value < node.value < node.right.value:
        if node:
            print(node.value)
            pre_order(node.left)
            pre_order(node.right)
    else:
        print("это не двоичное дерево")
        

pre_order(tree)
