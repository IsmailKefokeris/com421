import heapq
from heapq import heappush, heappop
import collections
import sys

class Node():
    
    def __init__(self,name,parent):
        self.name = name
        self.dist = sys.maxsize
        self.data = (self.dist, self)
        self.parent = parent
        self.used = False
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


    def __lt__(self, other):
        return self.name < other.name

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
        cur_node.data = (0, start)
        queue = []
        route = collections.deque([])
        heappush(queue,cur_node.data)

        while cur_node != end and len(queue) > 0:
            for edges in cur_node.edges:
                if edges.end.used == False:
                    distance = edges.dist + cur_node.data[0]
                    if distance < edges.end.data[0]:
                        edges.end.data = (distance, edges.end)
                        heappush(queue,edges.end.data)
                        edges.end.parent = cur_node
            cur_node.used = True
            new_node = heappop(queue)
            cur_node = new_node[1]
        
        while cur_node is not None:
            route.appendleft(cur_node.name) # add to front of deque
            cur_node = cur_node.parent
        return route




if __name__ == "__main__":
    n1 = Node("london",None)
    n2 = Node("Paris",n1)
    n3 = Node("Brussels",n1)
    n4 = Node("Amsterdam",n3)
    n5 = Node("Cologne",n3)
    n6 = Node("Frankfurt",n5)
    n7 = Node("Stuttgart",n2)
    n8 = Node("Munich",n7)

    graph = Graph()

    graph.add_edge(n1,n2,461)
    graph.add_edge(n1,n3,370)
    graph.add_edge(n2,n3,305)
    graph.add_edge(n2,n7,624)
    graph.add_edge(n2,n6,572)
    graph.add_edge(n3,n4,211)
    graph.add_edge(n3,n5,211)
    graph.add_edge(n4,n5,263)
    graph.add_edge(n5,n6,190)
    graph.add_edge(n6,n7,207)
    graph.add_edge(n6,n8,393)

    print(graph.dijkstra(n1,n8))