class Node:
  def __init__(self,data):
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
  
  
  if 
  
    
  def find(self, data):
    if self.data == data:
      return True
    elif data < self.data and self.left:
      return self.left.find(data)
    elif data > self.data and self.right:
      return self.right.find(data)
    return False

class Binary_Search_Tree:
	def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
  def insert(self, data):
		if self.root:
			return self.root.insert(d)
		else:
			self.root = Node(d)
			return True
  
