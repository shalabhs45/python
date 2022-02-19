class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # function to add an to graph
    def addEdge(self, u,v, w):
        self.graph.append([u,v,w])

    #Print the solution
    def printArr(self,dist):
        print("Vertex Distance from ")
        for  i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
       # Initialize distance 
       dist = [float("Inf")] * self.V
       dist[src] = 0

       for _ in range(self.V - 1):
           for u,v,w in self.graph:
               if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                   dist[v] = dist[u]  + w

       for u, v, w in self.graph:
            if dist[u] !=  float("Inf") and dist[u] + w < dist[v]:
                print(" Negative Wight Cycle")
                return
        
       self.printArr(dist)

g = Graph(3)
g.addEdge(0,1,-1)
g.addEdge(0,2,2)
g.addEdge(1,2,3)
g.addEdge(1,2,2)
g.addEdge(2,1,5)
g.BellmanFord(0)
