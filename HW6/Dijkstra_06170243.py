from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
      
    def Dijkstra(self, s): 
        return False
        
    def Kruskal(self):
        return False


##### 參考網址1 https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
##### 參考網址2 https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
##### 參考網址3 https://blog.csdn.net/DavyHwang/article/details/46552655 
##### 參考網址4 https://www.itread01.com/content/1549051928.html
