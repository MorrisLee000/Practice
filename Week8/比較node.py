class linked_list_node:
  def __init__(self,data):
    self.data = data
    self.next = None   ##用next指定下一個node
    
    
class Tree_node:
  def __init__(self,data):
    self.data = data
    self.left = None   ##把next轉換成left和right來指定下一個node
    self.right = None
    
    
