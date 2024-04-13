import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

def stworz_graf(krawedzie):
    G = nx.Graph()
    G.add_edges_from(krawedzie)
    return G

def znajdz_sciezki(G, start, koniec):
    return list(nx.all_simple_paths(G, start, koniec))

def oblicz_stopnie_wierzcholkow(G):
    return dict(G.degree())

def rysuj_graf(G):
    nx.draw(G, with_labels=True)
    plt.savefig("graf.png")