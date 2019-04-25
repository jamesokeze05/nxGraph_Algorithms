import networkx as nx
from itertools import combinations
from Functions.bool_functions import is_independent
from Functions.global_properties import V, n



def maximum_independent_set(G):
    for k in range(n(G), 1, -1):
        for S in combinations(V(G), k):
            if is_independent(G,list( S)) == True:
                return list(S)
            
def independence_number(G):
    return len(maximum_independent_set(G))

G = nx.erdos_renyi_graph(10, .5)
nx.draw_networkx(G)

print(maximum_independent_set(G))