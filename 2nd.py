# -*- coding: utf-8 -*-

import networkx as nx


G = nx.random_graphs.barabasi_albert_graph(100, 2)   #生成一个n=1000，度为4的BA无标度网络
#G = nx.random_graphs.newman_watts_strogatz_graph(5000, 2, 1)
#nx.set_node_attributes(G, 'degree', 4)
#print G.degree(0)                                   #返回某个节点的度

#print G.degree()                                     #返回所有节点的度

#print nx.degree_histogram(G)    #返回图中所有节点的度分布序列（从1至最大度的出现频次）?

#print nx.betweenness_centrality(G)
#print nx.edge_betweenness_centrality(G)
#nx.write_gexf(G, 'BA_N=10_degree=4_01.gexf')