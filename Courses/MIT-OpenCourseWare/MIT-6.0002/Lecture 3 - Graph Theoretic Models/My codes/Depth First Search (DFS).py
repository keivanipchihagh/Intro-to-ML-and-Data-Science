""" Each node object """
class Node(object):
    def __init__(self, name):
        self.name = name        
    def getName(self):
        return self.name    
    def __str__(self):
        return self.name

""" Each edge object """
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSrc(self):
        return self.src
    def getDest(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + ' -> ' + self.dest.getName()

""" Graph object - Nodes are represented as keys in the dictionary """
class Digraph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSrc()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for node in self.edges:
            if name == node.getName():
                return node
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges:
                result = result + src.getName() + ' -> ' + dest.getName()
        return result[:-1]

""" Graph object - Subclass of the Digraph """
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        reverseEdge = Edge(edge.getDest(), edge.getSrc())
        Digraph.addEdge(self, reverseEdge)

""" Initialize the graph - Graph type can be either Digraph or Graph """
def buildCityGraph(Digraph):
    network = Digraph()
    for name in ('Boston', 'Providence', 'Denver', 'Phoenix', 'NY', 'LA', 'Chicago'):
        network.addNode(Node(name))

    network.addEdge(Edge(network.getNode('Boston'), network.getNode('Providence')))
    network.addEdge(Edge(network.getNode('Boston'), network.getNode('NY')))
    network.addEdge(Edge(network.getNode('Providence'), network.getNode('Boston')))
    network.addEdge(Edge(network.getNode('Providence'), network.getNode('NY')))
    network.addEdge(Edge(network.getNode('NY'), network.getNode('Chicago')))
    network.addEdge(Edge(network.getNode('Chicago'), network.getNode('Denver')))
    network.addEdge(Edge(network.getNode('Chicago'), network.getNode('Phoenix')))
    network.addEdge(Edge(network.getNode('Denver'), network.getNode('Phoenix')))
    network.addEdge(Edge(network.getNode('Denver'), network.getNode('NY')))
    network.addEdge(Edge(network.getNode('LA'), network.getNode('Boston')))
    return network

""" Depth First Search (DFS) algorithm """
def DFS(graph, start, end, path, shortestPath, printDetails):
    path = path + [start]

    if printDetails:
        print('Current DFS path:', printPath(path))

    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:    # Avoid cycles
            if shortestPath == None or len(path) < len(shortestPath):
                newPath = DFS(graph, node, end, path, shortestPath, printDetails)
                if newPath != None:
                    shortestPath = newPath
        elif printDetails:
            print('Already traversed', node)            
    return shortestPath

""" Prints a path """
def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + ' -> '
    return result

""" Run the DFS using this function """
def getShortestPath(graph, start, end, printDetails):
    return DFS(graph, start, end, [], None, printDetails)

""" Test the DFS using this function """
def testShortestPath(source, destination):
    graph = buildCityGraph(Digraph)
    shortestPath = getShortestPath(graph, graph.getNode(source), graph.getNode(destination), True)

    if shortestPath != None:
        print('Shortest path from', source, 'to', destination, 'is:', printPath(shortestPath))
    else:
        print('There is no path from', source, 'to', destination)

testShortestPath('Boston', 'Chicago')
