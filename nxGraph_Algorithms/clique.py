import networkx as nx
from Functions.bool_functions import *
from Functions.global_properties import *
from itertools import combinations

def maximum_clique(G):
    for k in range(n(G), 1, -1):
        for S in combinations(V(G), k):
            if is_clique(G, list(S)) == True:
                return list(S)
            
def clique_numbers(G):
    return len(maximum_clique(G))


