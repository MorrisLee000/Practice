class Node:
    def __init__(self, nums):
        self.nums = nums
        self.left = None
        self.right = None

 class Binary_Search_Tree:
    def __init__(self, root):
        self.root = None
    
##插入
    def insert(self, nums)
        if self.root == None:
            self.root = Node(nums)
        else:
            self._insert(nums, self.root)
    
    def _insert(self, nums, cur_node):
        if nums > cur_node.nums:
            if cur_node.left == None:
                cur_node.left = Node(nums)
            else:
                self._insert
##刪除


##尋找


##取代
