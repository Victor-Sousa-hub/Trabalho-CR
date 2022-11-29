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

def random_network(length):
    G = nx.Graph()
    for i in range(length):
        j = random.randint(0,length-1)
        G.add_edge(i,j)
    return G

def malware(graph,node):
    save_edges = []
    if node < graph.size():
        try:
            save_edges.append(list(graph.edges(node)))
        except:
            pass
        graph.remove_node(node)
        return save_edges
    else:
        return None
def recovery(save_edges):
    for i in range(len(save_edges)):
        for j in range(len(save_edges[i])):
            G.add_edge(save_edges[i][j][0],save_edges[i][j][1])

def random_attack(graph,size):
    edges = []
    for i in range(size):
        node = random.randint(0,graph.size()) #escolhe um nó aleatório.
        try: #Tratamento de exceção:caso o nó ja tenha sido excluido o programa apenas ignora.
            save_edges = malware(graph,node) #Realisa o ataque.
            edges.append(save_edges)#salva todas as arestas excluidas.
        except:
            pass
    return edges

def target_attack(graph,size):
    edges = []
    for i in range(size):
        if(i % 2 == 0 and i != 0):
            save_edges = malware(graph,i)
            edges.append(save_edges)
    return edges

hub_network = hub_network(600,20) #criando uma rede com 1000 nós e cada hub aceita até 20 conexões
random_network = random_network(500) #criando uma rede com 500 nós aleatorios
nx.draw(hub_network,with_labels=False,node_size=40,font_size=10)
nx.draw(random_network,with_labels=False,node_size=20)
random_attack(random_network,50)
random_attack(hub_network,50)
nx.draw(hub_network,with_labels=False,node_size=40,font_size=10)
nx.draw(random_network,with_labels=False,node_size=20)
target_attack(random_network,50)
target_attack(hub_network,50)
nx.draw(hub_network,with_labels=False,node_size=40,font_size=10)
nx.draw(random_network,with_labels=False,node_size=20)
hub_network.remove_node(0)
nx.draw(hub_network,with_labels=False,node_size=40,font_size=10)
