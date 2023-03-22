import networkx as nx


def graph_types (G):
    graph_types = []

    if G == None:
        graph_types.append("Nulo")

    if G.number_of_edges() == 0:
        graph_types.append("Trivial")

    if (G.number_of_edges() == len(list(G.nodes())) or (G.number_of_edges() == 0)) or (len(list(G.nodes())) == 0):
        graph_types.append("Simples")

    if G.number_of_selfloops() != 0:
        graph_types.append("Pseudografo")

    return graph_types