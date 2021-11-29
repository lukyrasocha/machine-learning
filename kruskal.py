import networkx as nx
from uf import WeightedQuickUnionWithPathCompressionUF as UF

def Kruskal(Graph):
    edges=sorted(Graph.edges(data=True), key=lambda t: t[2]['weight'])
    maximum = max(list(map(lambda f: int(f),Graph.nodes())))+1
    unions = UF(maximum)
    
    mst = []
    for edge in edges:
        u = int(edge[0])
        v = int(edge[1])
        if not unions.connected(u,v):
            mst.append(edge)
            unions.union(u,v)
    return mst


if __name__ == '__main__':
    G = nx.read_weighted_edgelist('edge_list.txt')

    #Networkx - to check whether we get the correct result
    mst = nx.minimum_spanning_tree(G, weight='weight')
    own_mst = Kruskal(G)

    if len(own_mst) == len(mst.edges()):
        print('True')
