class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
class Solution(object):
    def __init__(self):
        self.root = root
    ##新增
    def insert(self, root, val):
        if self.root == None:                    ##判斷self.root是否為None，如果是的話，self.root = TreeNode(val)
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)
    
    def _insert(self, val, c_node):
        if val <= c_node.val:                    ##判斷val的大小來決定要把它放到哪邊
            if c_node.left == None:              ##判斷完val後，去看left和right是否有東西，如果沒有的話，val放到那個位置
                c_node.left = TreeNode(val)
            else:
                self._insert(val, c_node.left)   ##如果left和right已經有東西了，就重複呼交function直到它放進去
        elif val > c_node.val:
            if c_node.right == None:
                c_node.right = TreeNode(val)
            else:
                self._insert(val, c_node.right)
    ##尋找
    def search(self, root, target):
        if self.root != None:                              ##判斷self.root是否有東西，如果有就進到_search的function
            self._search(target, self.root)                ##如果沒有就回傳None
        else:
            return None
            
    def _search(self, target, c_node):
        if target == c_node.val:                           ##假設target == c_node.val，回傳c_node
            return c_node.val
        elif target < c_node.val and c_node.left != None:  ##如果target != c_node.val，先比較大小，然後決定往左邊或
            return self._search(target, c_node.left)       ##右邊繼續找下去，如果都沒有就回傳None
        elif target > c_node.val and c_node.right != None:
            return self._search(target, c_node.right)
        else:
            return None    
    ##刪除
    def delete(self, root, target):
        return self._delete(self.search(target, self.root))
    
    def _delete(self, TreeNode):
        if TreeNode == None or self.search(TreeNode.val) == None:  ##如果刪除的目標沒再tree裡面就回傳None
            return None
        
        def min_val_node(i):        ##回傳整棵樹的最小值
            cur = i
            while cur.left != None:
                cur = cur.left
                return cur
        
        def child_num(i):       ##回傳child的數量
            child_num = 0
            if i.left != None:
                child_num += 1
            if i.right != None:
                child_num += 1
            return child_num
        
        node_parent = TreeNode.parent    ##找到欲刪除節點的parent
        
        node_child = child_num(TreeNode) ##找到欲刪除節點的child數量
        ##假設沒有child
        if node_child == 0:
            if node_parent != None:      ##移除欲刪除的目標節點
                node_parent.left = None
            else:
                node_parent.right = None
        else:
            self.root = None
        ##假設有一個child
        if node_child == 1:
            if TreeNode.left != None:   ##判斷child的位置，因為只有一個child，所以只要判斷在哪邊
                child = TreeNode.left
            else:
                child = TreeNode.right
            
            if node_parent != None:     ##用child來取代刪除的節點
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
            TreeNode.val = cho.val             ##使用較小的節點來代替刪除的節點
            self._delete(cho)
        return self.delete(root, target)       ##因為要刪除所有相同的數值，因此要重新呼delete    
    ##修改
    def modify(self, root, target, new_node):
        return None
        
        
        
##參考網址1 https://www.youtube.com/watch?v=f5dU3xoE6ms
##參考網址2 https://www.youtube.com/watch?v=Zaf8EOVa72I
##參考網址3 https://github.com/bfaure/Python3_Data_Structures/blob/master/Binary_Search_Tree/main.py
