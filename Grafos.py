import networkx as nx
import random 
import matplotlib.pyplot as plt 
import pandas as pd
import sys

def hub_network(length_network,length_hub):
    G = nx.Graph()
    for i in range(length_network):
        if(i%length_hub == 0):
            j = 0
            G.add_edge(i,j)
            j = i
            G.add_node(j)
        if(i != j):
            G.add_edge(i,j)
    return G
