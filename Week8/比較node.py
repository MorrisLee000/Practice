class Node:
    def __init__(self,data):
        self.data = data
        self.left = None   ##把next轉換成left和right來指定下一個node
        self.right = None
----------------------------------------------------------------    
class Tree:
    def __init__(self):
        self.val = None
        
    def get(self.index):
        if self.val == None:
            return -1
        if index == 0:
            return self.val
        i = 1
        while self.left != None:
            if i == index:
                return self.left.val
            self.left = self.left.left
            i += 1
        return -1
        while self.right != None:
            if i == index:
                return self.right.val
            self.right = self.right.right
            i += 1
        return -1
  
  def addAtTail(self,val):
  
  ##參考老師的linkedlist
  ##參考網址https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
  ##參考網址https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
