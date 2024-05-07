import sys
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[]for _ in range(vertices)]

    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))

    def prim_algo(self):
        key=[sys.maxsize]*self.v
        parent=[-1]*self.v
        mst_set=[False]*self.v
        key[0]=0
        for _ in range(self.v):
            u = self.min_key(key,mst_set)
            mst_set[u] = True

            for v,w in self.graph[u]:
                if not mst_set[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        self.print_mst(parent)

    def min_key(self , key , mst_set):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.v):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index=v

        return min_index

    def print_mst(self,parent):
        print("Edge \tWeight")
        for i in range(1,self.v):
            print(parent[i],"-",i,"\t",self.get_weight(parent[i],i))

    def get_weight(self,u,v):
        for vertex , weight in self.graph[u]:
            if vertex == v:
                return weight
        return None

# Example usage:
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.prim_algo()