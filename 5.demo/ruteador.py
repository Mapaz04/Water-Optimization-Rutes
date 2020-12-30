import networkx as nx

def Roptima(G,source1,target1,weight1):
    route = nx.shortest_path(G, source=source1, target=target1, weight=weight1, method='dijkstra')
    return route

