def candidates (G,v):
    not_neighbor = []

    if G is not None and v is not None:
        nodes = list(G.nodes)

        if v not in nodes:
            return None

        neighbors = list(G.neighbors(v))

    else:
        return None

    for n in nodes:
        if (n not in neighbors and n != v) or (len(nodes) == 1):
            not_neighbor.append(n)

    return sorted(not_neighbor)