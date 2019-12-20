from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s): 
        array1 = []
        array2 = []
        array2.append(s)
        while len(array2) != len(self.graph):
            for i in self.graph[s]:
                if array1.count(i)==0 and array2.count(i)==0:
                    array1.append(i)
                else:
                    pass
            array2.append(array1[0])
            array1.pop(0)
            s = array2[-1]
        return array2
    
    def DFS(self, s):
        array1 = []
        array2 = []
        array2.append(s)
        while len(array2) != len(self.graph):
            for i in self.graph[s]:
                if array1.count(i)==0 and array2.count(i)==0:
                    array1.append(i)
                else:
                    pass
            array2.append(array1[-1])
            array1.pop(-1)
            s = array2[-1]
        return array2

#### https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
#### https://super9.space/archives/1562
#### https://www.programiz.com/dsa/graph-bfs
#### https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python/43869149
#### https://www.itread01.com/content/1542363063.html
#### https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
