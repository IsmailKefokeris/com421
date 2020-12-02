import heapq
from heapq import heappush, heappop
import sys

class Node():
    
    def __init__(self,name,parent):
        self.name = name
        self.dist = sys.maxsize
        self.data = (self, self.dist)
        self.parent = parent
        self.used = False
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


    def __lt__(self,other):
        pass

class Edge():
    
    def __init__(self, start, end, dist):
        self.start = start
        self.end = end
        self.dist = dist

class Graph():
    
    def add_edge(self, start, end, dist):
        edge = Edge(start, end, dist)
        edge2 = Edge(end, start, dist)
        start.add_edge(edge)
        end.add_edge(edge2)

    def dijkstra(self, start, end):
        cur_node = start
        cur_node.data = (start, 0)
        queue = []
        heappush(queue,cur_node.data)

        while cur_node != end and len(queue) > 0:
            for edges in cur_node.edges:
                if edges.end.used != True:
                    distance = edges.dist + cur_node.data[1]
                    if distance < edges.end.data[1]:
                        pass
                else:
                    pass



if __name__ == "__main__":
    n1 = Node("london",None)
    n2 = Node("Birmingham",n1)
    n3 = Node("Walsall",n2)
    n4 = Node("Southampton",n1)
    n5 = Node("Liverpool",n2)
    n6 = Node("Bristol",n5)

    graph = Graph()

    graph.add_edge(n1,n2,235)
    graph.add_edge(n2,n3,25)
    graph.add_edge(n3,n5,155)
    graph.add_edge(n2,n5,125)
    graph.add_edge(n1,n4,105)
    graph.add_edge(n5,n6,255)
    graph.add_edge(n4,n6,235)

    graph.dijkstra(n1,n6)