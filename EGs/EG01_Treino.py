import networkx as nx

#Criando Grafo aleatório para treino (Grafo Completo)
test_Complete_Graph = nx.complete_graph(10)

#Listando Nodes
nodes = test_Complete_Graph.nodes
print(nodes)

#Listando Arestas
edges = test_Complete_Graph.edges()
print(edges)

#Classificando Grafos
test_Complete_Graph