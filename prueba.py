from turtle import back
from numpy import save
from algorithms import *
import random
from graph import *
# # cuales ya: geográfico, gilbert, erdos (con muchas aristas),
# g = gridGraph(6)
# # funcion para arbol BFS
# # input: El grafo, el nodo s
# # output: lista de capas L[0], L[1],...,L[i] y el árbol BFS

# g = gridGraph(6)
# g = geographicGraph(30, r=0.5)
# g = barasiAlbertGraph(30, 4)
# g = dorogovtsevMendesGraph(30)
# g = gilbertGraph(500, p=0.6)
# g = erdosRenyiGraph(30, 500)
# s = 7
# tree = Graph()
# visited = [False] * len(g.nodes.keys())
# visited[s] = True
# tree.addNode(s)
# tree.typee = 6
# L = []
# Ls = []
# L.append(s)
# Ls.append([s])

# while L:
#     s = L.pop(0)
#     vecinos = g.nodes[s].attr['NEIGHBORS']
#     for vecino in vecinos:
#         # print(vecino.id)
#         L_i = []
#         if visited[vecino.id] == False:
#             # print(vecino.id)
#             L.append(vecino.id)
#             visited[vecino.id] = True
#             tree.addEdge(s, vecino.id, f"{s}->{vecino.id}")
#             L_i.append(vecino.id)

# saveGraph(tree, g.typee)

# g = erdosRenyiGraph(100, 4500)
# g = gridGraph(6)
# g = geographicGraph(30, r=0.6)
# print(s)


def DFS_R(g, s):
    tree = Graph()
    visited = set()
    tree.typee = 7
    t = DFS_UTILS(g, s, tree, visited)
    return t


def DFS_UTILS(g, s, tree, visited):
    visited.add(s)
    vecinos = g.nodes[s].attr['NEIGHBORS']
    random.shuffle(vecinos)
    for vecino in vecinos:
        if vecino.id not in visited:
            tree.addEdge(s, vecino.id, f'{s}->{vecino.id}')
            DFS_UTILS(g, vecino.id, tree, visited)
    return tree


def DFS_I(g, s):
    tree = Graph()
    discovered = [s]
    u = s
    stack = []
    while True:
        vecinos = g.nodes[u].attr['NEIGHBORS']
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

    # print()
    # print(discovered_idx)

# g = geographicGraph(500, r=0.6)
# tree = Graph()
# tree.typee = 8
# visited = [False] * len(g.nodes.keys())
# for i in range(len(g.nodes.keys())):
#     DFS_IF(i, tree, visited)


# saveGraph(tree, t_g=g.typee)
# g = Graph()
# g.typee = 9
# g.addEdge(0, 1, f'0->1')
# g.addEdge(0, 2, f'0->2')
# g.addEdge(2, 1, f'2->1')
# g.addEdge(1, 3, f'1->3')
# g.addEdge(1, 4, f'1->4')
# g.addEdge(2, 5, f'2->5')
# g.addEdge(4, 5, f'4->5')
# tree = DFS_R(0)
# tree.typee = 7
# saveGraph(tree, g.typee)
# g = geographicGraph(500, r=0.25)
# g = barasiAlbertGraph(500, 30)
# g = barasiAlbertGraph(100, 12)
g = barasiAlbertGraph(30, 4)
# g = gridGraph(6)
# g = erdosRenyiGraph(100, 4500)
# g = dorogovtsevMendesGraph(30)
# g = gilbertGraph(500, p=0.3)
# tree = DFS_R(g, 5)
# saveGraph(tree, g.typee)
# tree = DFS_I(g, 5)
# tree.typee = 8
# saveGraph(tree, g.typee)
tree = DFS_I(g, 5)
tree.typee = 8
saveGraph(tree, g.typee)
