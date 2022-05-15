





                        1
                      /   \
                     2     3
                   /   \  
                  4     5
                  
                  
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.reght = None
    
    
tree =            TreeNode(1)
tree.left =       TreeNode(2)
tree.right =      TreeNode(3)
tree.left.left =  TreeNode(4)
tree.left.right = TreeNode(5)

