from edge import Edge
from node import Node
import random


class Graph:
    def __init__(self):
        self.nodes = {}  # Graph nodes
        self.edges = {}  # Graph edges
        self.typee = None  # Type of graph
        self.attr = {}

    def addNode(self, name):
        """
        Add node to graph.
        :param name: the name of the node
        """
        # First check if node already exists
        n = self.nodes.get(name)

        if n is None:
            n = Node(name)

            self.nodes[name] = n
            # print("se crea nodo", name)
        # else:
        #     print("el nodo ", name, "ya existia")

        return n

    def addEdge(self, s, t, label):
        """
        Add edge to graph.
        :param s: source node
        :param t: target node
        :param label: s->t
        """
        e = self.edges.get(label)

        if e is None:
            n1 = self.addNode(s)
            n2 = self.addNode(t)
            e = Edge(n1, n2, label)

            self.edges[label] = e
            n1.attr["NEIGHBORS"].append(n2)
            n1.attr['EDGES'].append(e)
            n2.attr["NEIGHBORS"].append(n1)
            n2.attr['EDGES'].append(e)

        return e

    def getNodes(self):
        """
        Return list of nodes
        """
        total_nodes = list(self.nodes.keys())
        return total_nodes

    def getEdges(self):
        """
        Return list of edges
        """
        total_edges = [[edge.s.id, edge.t.id] for edge in self.edges.values()]
        return total_edges

    def BFS(self, s):
        """
        Applies BFS algorithm to graph
        s: source node (int)

        return tree (Graph), List of tree layers, label graph (for saving)
        """
        tree = Graph()
        visited = [False] * len(self.nodes.keys())
        visited[s] = True
        tree.addNode(s)
        tree.typee = 6
        L = []
        Ls = []
        L.append(s)
        Ls.append([s])

        while L:
            s = L.pop(0)
            vecinos = self.nodes[s].attr['NEIGHBORS']
            L_i = []
            for vecino in vecinos:
                # print(vecino.id)
                if visited[vecino.id] == False:
                    # print(vecino.id)
                    L.append(vecino.id)
                    visited[vecino.id] = True
                    tree.addEdge(s, vecino.id, f"{s}->{vecino.id}")
                    L_i.append(vecino.id)
            if len(L_i) > 0:
                Ls.append(L_i)

        return tree, Ls, self.typee

    def DFS_UTILS(self, s, tree, visited):
        visited.add(s)
        vecinos = self.nodes[s].attr['NEIGHBORS']
        random.shuffle(vecinos)
        for vecino in vecinos:
            if vecino.id not in visited:
                tree.addEdge(s, vecino.id, f'{s}->{vecino.id}')
                self.DFS_UTILS(vecino.id, tree, visited)
        return tree

    def DFS_R(self, s):
        """
        Applies recursive DFS algorithm to graph
        s: source node (int)

        return tree (Graph)

        """
        tree = Graph()
        visited = set()
        tree.typee = 7
        t = self.DFS_UTILS(s, tree, visited)
        return t

    def DFS_I(self, s):
        """
        Applies iterative DFS algorithm to graph
        s: source node (int)

        return tree (Graph)

        """
        tree = Graph()
        tree.typee = 8
        discovered = [s]
        u = s
        stack = []
        while True:
            vecinos = self.nodes[u].attr['NEIGHBORS']
            for vecino in vecinos:
                if vecino.id not in discovered:
                    stack.append(vecino.id)

            if not stack:
                break

            p, c = u, stack.pop()
            if c not in discovered:
                tree.addEdge(p, c, f"{p}->{c}")
                discovered.append(c)
            u = c

        return tree
