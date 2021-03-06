from numpy import save
from algorithms import *

if __name__ == "__main__":
    # ################################## PARTE 1 ######################################
    # g = gridGraph(23)
    # saveGraph(g)
    ##################################
    # g = erdosRenyiGraph(500, 2500)
    # saveGraph(g)
    # ##################################
    # g = gilbertGraph(500, p=0.6)
    # saveGraph(g)
    ##################################
    # g = geographicGraph(30, r=0.5)
    # print(list(g.nodes.keys()))
    # saveGraph(g)
    ##################################
    # g = barasiAlbertGraph(30, 4)
    # saveGraph(g)
    # print(g.getEdges())
    ##################################
    # g = dorogovtsevMendesGraph(500)
    # saveGraph(g)

    ################# ################### PARTE 2 ##################################

    ###################### BFS #######################
    # g = barasiAlbertGraph(500, 87)
    # tree, g_label = g.BFS(7)
    # saveGraph(tree, g_label)
    ################################
    # g = dorogovtsevMendesGraph(500)
    # tree, Ls, g_label = g.BFS(106)
    # saveGraph(tree, g_label)
    ###############################
    # g = gilbertGraph(100, p=0.6)
    # tree, Ls, g_label = g.BFS(39)
    # print(len(Ls))
    # saveGraph(tree, g_label)
    ##############################
    # g = erdosRenyiGraph(100, 4500)
    # tree, Ls, g_label = g.BFS(52)
    # saveGraph(tree, g_label)
    ###############################
    # g = barasiAlbertGraph(100, 24)
    # tree, Ls, g_label = g.BFS(19)
    # saveGraph(tree, g_label)
    ###############################
    # g = gridGraph(23, 23)
    # tree, Ls, g_label = g.BFS(511)
    # saveGraph(tree, g_label)
    ################################
    # g = geographicGraph(30, r=0.3)
    # tree, Ls, g_label = g.BFS(23)
    # saveGraph(tree, g_label)
    ###############################
    # g = gridGraph(23)
    # tree, Ls, g_label = g.BFS(371)
    # saveGraph(tree, g_label)
    ###############################
    # g = erdosRenyiGraph(500, 122000)
    # tree, Ls, g_label = g.BFS(331)
    # saveGraph(tree, g_label)
    ##############################DFS########################
    # g = geographicGraph(30, r=0.25)
    # tree = g.DFS_R(4)
    # saveGraph(tree, g.typee)
    ###########################################################
    # g = dorogovtsevMendesGraph(30)
    # tree = g.DFS_R(12)
    # saveGraph(tree, g.typee)
    ###########################################################
    # g = dorogovtsevMendesGraph(100)
    # tree = g.DFS_R(55)
    # saveGraph(tree, g.typee)
    ###############################
    # g = barasiAlbertGraph(30, 11)
    # tree, Ls, g_label = g.BFS(2)
    # saveGraph(tree, g_label)
    ###############################
    # g = erdosRenyiGraph(30, 400)
    # tree = g.DFS_R(22)
    # saveGraph(tree, g.typee)
    ###############################
    # g = gilbertGraph(30, 0.3)
    # tree = g.DFS_R(19)
    # saveGraph(tree, g.typee)
    ###############################
    # g = gilbertGraph(100, 0.25)
    # tree = g.DFS_R(66)
    # saveGraph(tree, g.typee)
    ###############################
    # g = gridGraph(10, 10)
    # tree = g.DFS_R(44)
    # saveGraph(tree, g.typee)
    ###############################
    # g = gridGraph(23, 23)
    # tree = g.DFS_R(333)
    # saveGraph(tree, g.typee)
    ###############################
    # g = erdosRenyiGraph(500, 100000)
    # tree = g.DFS_R(432)
    # saveGraph(tree, g.typee)
    ###############################DFS I ##############################
    # g = dorogovtsevMendesGraph(30)
    # tree = g.DFS_I(22)
    # saveGraph(tree, g.typee)
    # ###################################
    # g = erdosRenyiGraph(30, 400)
    # tree = g.DFS_I(18)
    # saveGraph(tree, g.typee)
    # ###################################
    # g = gilbertGraph(30, 0.25)
    # tree = g.DFS_I(5)
    # saveGraph(tree, g.typee)
    # ##################################
    # g = geographicGraph(500, r=0.25)
    # tree = g.DFS_I(8)
    # saveGraph(tree, g.typee)
    ##################################
    # g = gridGraph(6, 6)
    # tree = g.DFS_I(1)
    # saveGraph(tree, g.typee)
    ##################################
    # g = geographicGraph(100, r=0.25)
    # tree = g.DFS_I(7)
    # saveGraph(tree, g.typee)
    # ###################################
    # g = gilbertGraph(500, 0.20)
    # tree = g.DFS_I(444)
    # saveGraph(tree, g.typee)
    ####################################
    # g = barasiAlbertGraph(500, 21)
    # tree = g.DFS_I(13)
    # saveGraph(tree, g.typee)
    ###############################DFS I ##############################
    # g = dorogovtsevMendesGraph(500)
    # tree = g.DFS_I(300)
    # saveGraph(tree, g.typee)
    # ###################################
    # g = erdosRenyiGraph(500, 8500)
    # tree = g.DFS_I(444)
    # saveGraph(tree, g.typee)
    ##################################

    # ### grid ###
    # g1 = gridGraph(6, 6)
    # saveGraph(g1)
    # tree1, Ls = g1.BFS(22)
    # saveGraph(tree1, g1.typee)
    # tree2 = g1.DFS_I(22)
    # saveGraph(tree2, g1.typee)
    # tree3 = g1.DFS_R(22)
    # saveGraph(tree3, g1.typee)
    # g2 = gridGraph(10, 10)
    # saveGraph(g2)
    # tree4, Ls = g2.BFS(57)
    # saveGraph(tree4, g2.typee)
    # tree5 = g2.DFS_I(57)
    # saveGraph(tree5, g2.typee)
    # tree6 = g2.DFS_R(57)
    # saveGraph(tree6, g2.typee)
    # g3 = gridGraph(23, 23)
    # saveGraph(g3)
    # tree7, Ls = g3.BFS(386)
    # saveGraph(tree7, g3.typee)
    # tree8 = g3.DFS_I(386)
    # saveGraph(tree8, g3.typee)
    # tree9 = g3.DFS_R(386)
    # saveGraph(tree9, g3.typee)

    ### barasialbert ###
    # g1 = barasiAlbertGraph(30, 3)
    # saveGraph(g1)
    # tree1, Ls = g1.BFS(22)
    # saveGraph(tree1, g1.typee)
    # tree2 = g1.DFS_I(22)
    # saveGraph(tree2, g1.typee)
    # tree3 = g1.DFS_R(22)
    # saveGraph(tree3, g1.typee)
    # g2 = barasiAlbertGraph(100, 16)
    # saveGraph(g2)
    # tree4, Ls = g2.BFS(57)
    # saveGraph(tree4, g2.typee)
    # tree5 = g2.DFS_I(57)
    # saveGraph(tree5, g2.typee)
    # tree6 = g2.DFS_R(57)
    # saveGraph(tree6, g2.typee)
    # g3 = barasiAlbertGraph(500, 41)
    # saveGraph(g3)
    # tree7, Ls = g3.BFS(386)
    # saveGraph(tree7, g3.typee)
    # tree8 = g3.DFS_I(386)
    # saveGraph(tree8, g3.typee)
    # tree9 = g3.DFS_R(386)
    # saveGraph(tree9, g3.typee)

    ### geographic ###
    # g1 = geographicGraph(30, 0.4)
    # saveGraph(g1)
    # tree1, Ls = g1.BFS(22)
    # saveGraph(tree1, g1.typee)
    # tree2 = g1.DFS_I(22)
    # saveGraph(tree2, g1.typee)
    # tree3 = g1.DFS_R(22)
    # saveGraph(tree3, g1.typee)
    # g2 = geographicGraph(100, 0.4)
    # saveGraph(g2)
    # tree4, Ls = g2.BFS(57)
    # saveGraph(tree4, g2.typee)
    # tree5 = g2.DFS_I(57)
    # saveGraph(tree5, g2.typee)
    # tree6 = g2.DFS_R(57)
    # saveGraph(tree6, g2.typee)
    # g3 = geographicGraph(500, 0.4)
    # saveGraph(g3)
    # tree7, Ls = g3.BFS(294)
    # saveGraph(tree7, g3.typee)
    # tree8 = g3.DFS_I(294)
    # saveGraph(tree8, g3.typee)
    # tree9 = g3.DFS_R(294)
    # saveGraph(tree9, g3.typee)

    ### Erdosreyni ###
    # g1 = erdosRenyiGraph(30, 280)
    # saveGraph(g1)
    # tree1, Ls = g1.BFS(22)
    # saveGraph(tree1, g1.typee)
    # tree2 = g1.DFS_I(22)
    # saveGraph(tree2, g1.typee)
    # tree3 = g1.DFS_R(22)
    # saveGraph(tree3, g1.typee)
    # g2 = erdosRenyiGraph(100, 2500)
    # saveGraph(g2)
    # tree4, Ls = g2.BFS(38)
    # saveGraph(tree4, g2.typee)
    # tree5 = g2.DFS_I(38)
    # saveGraph(tree5, g2.typee)
    # tree6 = g2.DFS_R(38)
    # saveGraph(tree6, g2.typee)
    # g3 = erdosRenyiGraph(500, 32300)
    # saveGraph(g3)
    # tree7, Ls = g3.BFS(197)
    # saveGraph(tree7, g3.typee)
    # tree8 = g3.DFS_I(197)
    # saveGraph(tree8, g3.typee)
    # tree9 = g3.DFS_R(197)
    # saveGraph(tree9, g3.typee)

    ### Gilbert ###
    # g1 = gilbertGraph(30, 0.2)
    # saveGraph(g1)
    # tree1, Ls = g1.BFS(22)
    # saveGraph(tree1, g1.typee)
    # tree2 = g1.DFS_I(22)
    # saveGraph(tree2, g1.typee)
    # tree3 = g1.DFS_R(22)
    # saveGraph(tree3, g1.typee)
    # g2 = gilbertGraph(100, 0.2)
    # saveGraph(g2)
    # tree4, Ls = g2.BFS(84)
    # saveGraph(tree4, g2.typee)
    # tree5 = g2.DFS_I(22)
    # saveGraph(tree5, g2.typee)
    # tree6 = g2.DFS_R(22)
    # saveGraph(tree6, g2.typee)
    # g3 = gilbertGraph(500, 0.2)
    # saveGraph(g3)
    # tree7, Ls = g3.BFS(196)
    # saveGraph(tree7, g1.typee)
    # tree8 = g3.DFS_I(196)
    # saveGraph(tree8, g1.typee)
    # tree9 = g3.DFS_R(196)
    # saveGraph(tree9, g3.typee)

    ### Gilbert ###
    g1 = dorogovtsevMendesGraph(30)
    saveGraph(g1)
    tree1, Ls = g1.BFS(22)
    saveGraph(tree1, g1.typee)
    tree2 = g1.DFS_I(22)
    saveGraph(tree2, g1.typee)
    tree3 = g1.DFS_R(22)
    saveGraph(tree3, g1.typee)
    g2 = dorogovtsevMendesGraph(100)
    saveGraph(g2)
    tree4, Ls = g2.BFS(84)
    saveGraph(tree4, g2.typee)
    tree5 = g2.DFS_I(84)
    saveGraph(tree5, g2.typee)
    tree6 = g2.DFS_R(84)
    saveGraph(tree6, g2.typee)
    g3 = dorogovtsevMendesGraph(500)
    saveGraph(g3)
    tree7, Ls = g3.BFS(196)
    saveGraph(tree7, g1.typee)
    tree8 = g3.DFS_I(196)
    saveGraph(tree8, g1.typee)
    tree9 = g3.DFS_R(196)
    saveGraph(tree9, g3.typee)
