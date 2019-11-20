class Solution(object):
    ##新增
    def insert(self, root, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)
    
    def _insert(self, val, c_node):
        if val <= c_node.val:
            if c_node.left == None:
                c_node.left = TreeNode(val)
            else:
                self._insert(val, c_node.left)
        elif val > c_node.val:
            if c_node.right == None:
                c_node.right = TreeNode(val)
            else:
                self._insert(val, c_node.right)
    ##尋找
    def search(self, root, target):
        if self.root != None:                             
            self._search(target, self.root)               
        else:
            return None
            
    def _search(self, target, c_node):
        if target == c_node.val:                          
            return c_node
        elif target < c_node.val and c_node.left != None: 
            return self._search(target, c_node.left)      
        elif target > c_node.val and c_node.right != None:
            return self._search(target, c_node.right)
        else:
            return None
    ##刪除
    def delete(self, root, target):
        return self._delete(self.search(target))
    
    def _delete(self, TreeNode):
        if TreeNode == None or self.search(TreeNode.val) == None:
            return None
        
        def min_val_node(i):
            cur = i
            while cur.left != None:
                cur = cur.left
                return cur
        
        def child_num(i):
            child_num = 0
            if i.left != None:
                child_num += 1
            if i.right != None:
                child_num += 1
            return child_num
        
        node_parent = TreeNode.parent
        
        node_child = child_num(TreeNode)
        ##假設沒有child
        if node_child == 0:
            if node_parent != None:
                node_parent.left = None
            else:
                node_parent.right = None
        else:
            self.root = None
        ##假設有一個child
        if node_child == 1:
            if TreeNode.left != None:
                child = TreeNode.left
            else:
                child = TreeNode.right
            
            if node_parent != None:
                if node_parent.left == TreeNode:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child
            child.parent = node_parent
        ##假設有兩個child
        if node_child == 2:
            cho = min_val_node(TreeNode.right)
            TreeNode.val = cho.val
            self._delete(cho)
        return self.delete(root, target)
    ##取代
    def modify(self, root, target, new_node):
        
        
        
        
##參考網址1 https://www.youtube.com/watch?v=f5dU3xoE6ms
##參考網址2 https://www.youtube.com/watch?v=Zaf8EOVa72I
##參考網址3 https://github.com/bfaure/Python3_Data_Structures/blob/master/Binary_Search_Tree/main.py
