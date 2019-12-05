from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * self.capacity
    
    def add(self, key):
        h = MD5.new()                   
        h.update(key.encode("UTF-8"))   
        x = int(h.hexdigest(), 16)      
        k = x % self.capacity           
        target = self.data[k]           
        while target:                   
            if target.val == x:         
                return                  
            else:
                target = target.next    
        new_listnode = ListNode(x)      
        new_listnode.next = self.data[k]
        self.data[k] = new_listnode     
    
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("UTF-8"))
        x = int(h.hexdigest(),16)
        k = x % self.capacity
        target = self.data[k]        
        while target:
            if target.val == x:
                self.data[k] = target.next
                return
            else:
                previous = None
            while target:
                if target.val == x:
                    previous.next = target.next
                    return
                else:
                    previous = target
                    target = target.next
              
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("UTF-8"))
        x = int(h.hexdigest(), 16)
        k = x % self.capacity
        target = self.data[k]
        while target:
            if target.val == x:      
                return True          
            else:                    
                target = target.next
        return False


#參考網址1 https://www.youtube.com/watch?v=7C5f2ttq79Y&feature=youtu.be
#參考網址2 https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
#參考網址3 https://www.youtube.com/watch?v=zHi5v78W1f0
#參考網址4 https://www.youtube.com/watch?v=MfhjkfocRR0
#參考網址5 https://www.youtube.com/watch?v=KyUTuwz_b7Q
