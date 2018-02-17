# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('dolphins.gml')
klist = list(nx.k_clique_communities(G,3)) #list of k-cliques in the network. each element contains the nodes that consist the clique.

#plotting
pos = nx.spring_layout(G)
plt.clf()
nx.draw(G,pos = pos, with_labels=False)
nx.draw(G,pos = pos, nodelist = klist[0], node_color = 'b')
nx.draw(G,pos = pos, nodelist = klist[1], node_color = 'y')
plt.show()