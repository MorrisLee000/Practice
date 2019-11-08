class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data
    
  def find(self, val):
    if val < self.data:
      if self.left.data is None:
        return "Not Found"
      else:
        return self.left.find(self, val):
    elif val > self.data:
      if self.right.data is None:
        return "Not Found"
      else:
        return self.right.find(self, val):
    else:
      return "Found"
  
  def 
