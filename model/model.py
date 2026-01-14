import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.grafo=nx.Graph()
        self.lista_album=[]

    def crea_grafo(self, durata: int):
        self.grafo = nx.Graph()
        self.lista_album=DAO.read_album_per_durata(durata)
        for a in self.lista_album:
            self.grafo.add_node(a)
        lista_album_per_playlist= DAO.read_album_per_playlist()
        for a1, a2 in lista_album_per_playlist:
            if a1 in self.grafo and a2 in self.grafo:
                self.grafo.add_edge(a1, a2)

    def get_durata_tot(self, a1:int):
        lista_durate=[]
        comp= nx.node_connected_component(self.grafo, a1)
        for a in comp:
            lista_durate.append(DAO.read_durata(a))
        durata_tot=sum(lista_durate)
        return durata_tot